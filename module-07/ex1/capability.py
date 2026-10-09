import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target: str = "itself") -> str: ...


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str: ...

    @abc.abstractmethod
    def revert(self) -> str: ...
