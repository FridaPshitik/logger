from dotenv import load_dotenv
import json
import os

DEFAULT_PATH = "failed_logs/failed_logs.log"


class LocalLogsWriter:
    def __init__(self) -> None:
        self.path = self._get_failed_log_path()

    def _get_failed_log_path(self) -> str:
        path = self._load_path_from_env()
        if self._is_exists_failed_log_path(path):
            return path
        else:
            return DEFAULT_PATH

    def _load_path_from_env(self) -> str:
        load_dotenv()
        return os.getenv("FAILED_LOGS_FILE_PATH")

    def _is_exists_failed_log_path(self, path) -> bool:
        if path is not None and path != "":
            directory_path = os.path.dirname(path)
            self._create_failed_log_dir(directory_path)
            return os.path.isdir(directory_path)
        self._create_failed_log_dir("failed_logs")
        return False

    def _create_failed_log_dir(self, directory_path):
        os.makedirs(directory_path, exist_ok=True)

    def write_log_to_local(self, log: dict):
        log_string = json.dumps(log)
        with open(self.path, "a") as file:
            file.write(f"{log_string}\n")
