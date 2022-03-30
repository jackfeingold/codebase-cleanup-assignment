
from app.utils import to_usd

def test_to_usd():
    assert to_usd(44.7654) == "$44.77"
    assert to_usd(123456.836) == "$123,456.84"

from app.game import winnerDetermination

