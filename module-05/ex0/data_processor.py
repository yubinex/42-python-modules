import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._items: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool: ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None: ...

    def output(self) -> tuple[int, str]:
        if not self._items:
            raise IndexError("List is empty.")
        return self._items.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        items = data if isinstance(data, list) else [data]

        for item in items:
            # isinstance checks whether an item matches one of these
            # allowed types.
            # Unlike type(...), it also recognizes subclasses.
            if not isinstance(item, (int, float)):
                return False
        return True

    # Static typing treats int as compatible with float.
    def ingest(
        self, data: float | list[int] | list[float] | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._items.append((self._next_rank, str(item)))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        items = data if isinstance(data, list) else [data]

        for item in items:
            if not isinstance(item, str):
                return False
        return True

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._items.append((self._next_rank, item))
            self._next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        items = data if isinstance(data, list) else [data]

        for item in items:
            if not isinstance(item, dict):
                return False

            for key, value in item.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            converted_string = ""
            if "log_level" in item and "log_message" in item:
                converted_string = (
                    f"{item['log_level']}: {item['log_message']}"
                )
            else:
                converted_string = " ".join(item.values())
            self._items.append((self._next_rank, converted_string))
            self._next_rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(f" Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f" Got exception: {error}")

    numeric_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {numeric_data}")
    numeric.ingest(numeric_data)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    print(f" Trying to validate input 'Hello': {text.validate('Hello')}")
    print(f" Trying to validate input '42': {text.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_data}")
    text.ingest(text_data)
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    valid_log = {
        "log_level": "NOTICE",
        "log_message": "Connection to server",
    }
    print(f" Trying to validate a log entry: {log.validate(valid_log)}")
    log_data = [
        valid_log,
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f" Processing data: {log_data}")
    log.ingest(log_data)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
