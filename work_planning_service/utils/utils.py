from django.utils.crypto import get_random_string


def get_prefix_id(prefix_code: str) -> str:
    return f"{prefix_code}{get_random_string(16)}"
