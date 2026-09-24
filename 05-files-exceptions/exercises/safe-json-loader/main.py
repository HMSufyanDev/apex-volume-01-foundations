import json
from pathlib import Path


class InvalidDataError(Exception):
    pass


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise InvalidDataError("Expected JSON object.")

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    except json.JSONDecodeError as error:
        print(f"Invalid JSON in {path}")
        print(f"Details: {error}")
        return None

    except InvalidDataError as error:
        print(f"Unexpected data: {error}")
        return None

    else:
        print("JSON loaded successfully.")
        return data

    finally:
        print("Load operation finished.")

data_path = Path("data/example.json")

data = load_json(data_path)

print("Result:", data)