import pytest


@pytest.mark.parametrize(
    'n, expected',
    [(123402, "LUCKY"), (7755, "READY")]
)
def test(n, expected):
    result = solution(n)
    assert result == expected

def solution(n):
    mid = len(n) / 2
    score = 0
    for i, v in enumerate(n):
        if i < mid:
            score += v
        else:
            score -= v
    if score == 0:
        print("LUCKY")
    else:
        print("READY")