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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None: ...


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            handled = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            proc_name = processor.__class__.__name__
            readable_name = ""
            for char in proc_name:
                if char.isupper() and readable_name:
                    readable_name += " "
                readable_name += char
            print(
                f"{readable_name}: total {processor._next_rank} items "
                f"processed, remaining {len(processor._items)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            output_data: list[tuple[int, str]] = []
            for _ in range(nb):
                if not processor._items:
                    break

                output_data.append(processor.output())
            plugin.process_output(output_data)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        properties = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("{" + properties + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    csv_plugin = CSVPlugin()
    json_plugin = JSONPlugin()

    first_batch: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print("\nRegistering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)
    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    second_batch: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
