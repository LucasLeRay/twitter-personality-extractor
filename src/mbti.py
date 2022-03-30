from dataclasses import dataclass
import itertools

EXTRAVERSION = "extraversion"
INTUITION = "intuition"
THINKING = "thinking"
JUDGING = "judging"


@dataclass
class _Axis:
    """MBTI personality axis"""
    name: str
    initial: str
    opposite: str


class _MBTI:
    def __init__(self):
        self.extraversion = _Axis(EXTRAVERSION, "E", "I")
        self.intuition = _Axis(INTUITION, "N", "S")
        self.thinking = _Axis(THINKING, "T", "F")
        self.judging = _Axis(JUDGING, "J", "P")

    @property
    def axis(self):
        return [self.extraversion, self.intuition, self.thinking, self.judging]

    @property
    def types(self):
        axis = [(p.initial, p.opposite) for p in self.axis]
        personalities = itertools.product(*axis)
        return ["".join(p) for p in personalities]


mbti = _MBTI()
