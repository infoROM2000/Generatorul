from .utils import error_print


class CustomError(Exception):
    def __init__(self, message: str):
        error_print(f"[ERROR] {message}")
        super().__init__(message)
