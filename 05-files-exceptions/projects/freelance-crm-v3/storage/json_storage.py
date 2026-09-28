from pathlib import Path
import json
import shutil

from utils.exceptions import BackupError, InvalidDataError


class JsonStorage:

    def __init__(self, data_file: Path, backup_file: Path):
        self.data_file = data_file
        self.backup_file = backup_file

        # Make sure required directories exist
        self.data_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.backup_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def create_empty_data():
        return {
            "leads": [],
            "clients": [],
            "projects": [],
            "invoices": []
        }

    def storage_load(self):
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            data = self.create_empty_data()
            self.storage_save(data)
            return data

        except json.JSONDecodeError as error:
            raise InvalidDataError(
                f"Invalid JSON data in {self.data_file}"
            ) from error

    def storage_save(self, data):
        try:
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4
                )

        except (OSError, TypeError) as error:
            raise InvalidDataError(
                "Could not save data to storage."
            ) from error

    def create_backup(self):
        if not self.data_file.exists():
            raise BackupError(
                "Cannot create backup because data file does not exist."
            )

        try:
            shutil.copy2(
                self.data_file,
                self.backup_file
            )

        except OSError as error:
            raise BackupError(
                f"Could not create backup: {error}"
            ) from error