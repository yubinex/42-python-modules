from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


# Inheriting from str makes enum values behave
# like strings in Pydantic and output.
class Rank(str, Enum):
    """List the ranks a crew member can have."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Validate information about one mission crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validate a mission and its complete crew."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Check safety rules that depend on the full mission data."""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                member.years_experience >= 5 for member in self.crew
            )
            if experienced_count / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew")

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Show a valid mission and an invalid mission."""

    crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=35,
            specialization="Mission Command",
            years_experience=12,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=29,
            specialization="Engineering",
            years_experience=6,
        ),
    ]

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2026-06-01T09:00:00"),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Space Mission Crew Validation")
    print("=" * 41)
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")

    for member in valid_mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
        )

    print()
    print("=" * 41)
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime.fromisoformat("2026-07-01T09:00:00"),
            duration_days=30,
            crew=crew[1:],
            budget_millions=100.0,
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
