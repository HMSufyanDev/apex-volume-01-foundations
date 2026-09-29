from pathlib import Path
import json
import shutil

from utils.exceptions import BackupError, InvalidDataError


class JsonStorage:

    def __init__(self, crm_file: Path, backup_dir: Path):
        self.crm_file = crm_file
        self.backup_dir = backup_dir

        self.crm_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.backup_dir.mkdir(
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
            with self.crm_file.open(
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except FileNotFoundError:

            data = self.create_empty_data()

            self.storage_save(data)

            return data

        except json.JSONDecodeError as error:

            raise InvalidDataError(
                f"Invalid JSON data in {self.crm_file}"
            ) from error

    def storage_save(self, data):
        try:
            with self.crm_file.open(
                "w",
                encoding="utf-8"
            ) as file:

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

        if not self.crm_file.exists():

            raise BackupError(
                "Cannot create backup because data file does not exist."
            )

        try:
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

            backup_file = (
                self.backup_dir / f"crm_backup_{timestamp}.json"
            )

            shutil.copy2(
                self.crm_file,
                backup_file
            )

        except OSError as error:

            raise BackupError(
                f"Could not create backup: {error}"
            ) from error