import pytest
@pytest.mark.parametrize(
    'n, decks, expected',
    [5, [40, 80, 20, 10, 120], 520],
    [3, [10, 20, 40], 100]
)
def test(n, decks, expected):
    result = solution(n, decks)
    assert result == expected

def solution(n, decks):
    decks.sort()
    first = 0
    card_shuffle = []
    next = 0

    for i in range(n):
        if i == 0:
            first = decks[i]+decks[i+1]
            card_shuffle.append(first)
        elif i == 1:
            continue
        elif i > 1:
            next = first + decks[i]
            print(next)
            card_shuffle.append(next)
            first = next

    return sum(card_shuffle)