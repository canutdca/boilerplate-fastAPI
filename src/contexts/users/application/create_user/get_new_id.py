from typing import Tuple


def get_new_id(ids: Tuple[int]) -> int:
    max_id = max(ids)
    return max_id + 1
