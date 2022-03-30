from enum import Enum


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    # See https://www.cosmicpython.com/blog/2020-10-27-i-hate-enums.html
    def __str__(self):
        return str.__str__(self)
