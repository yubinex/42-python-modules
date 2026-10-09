from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


# Inheriting from str makes enum values behave
# like strings in Pydantic and output.
class ContactType(str, Enum):
    """List the possible ways aliens can make contact."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Validate a report of contact with aliens."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Check rules that depend on more than one field."""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals should include a received message"
            )

        return self


def main() -> None:
    """Show valid and invalid alien contact reports."""
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2026-01-15T10:30:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Alien Contact Log Validation")
    print("=" * 38)
    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Type: {valid_contact.contact_type.value}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print(f"Witnesses: {valid_contact.witness_count}")
    print(f"Message: '{valid_contact.message_received}'\n")

    print("=" * 38)
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.fromisoformat("2026-01-15T11:00:00"),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
