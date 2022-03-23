import pytest
@pytest.mark.parametrize(
    'n, m, k, x, array, expected',
    [
        12,
        [("Junkyu", 50, 60, 100),
         ("Sangkeun", 80, 60, 50),
         ("Sunyoung", 80, 70, 100),
         ("soong", 50, 60, 90),
         ("haebin", 50, 60, 100),
         ("Kangsoo", 60, 80, 100),
         ("Donghyuk", 80, 60, 100),
         ("Sei", 70, 70, 70),
         ("Wonseob", 70, 70, 90),
         ("Sanghyun", 70, 70, 80),
         ("nsj", 80, 80, 80),
         ("Taewhan", 50, 60, 90)
        ],
        ["Donghyuk",
         "Sangkeun",
         "Sunyoung",
         "nsj",
         "Wonseob",
         "Sanghyun",
         "Sei",
         "Kangsoo",
         "Junkyu",
         "haebin",
         "soong",
         "Taewhan"
        ]
    ]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


def solution(n, array):
    array.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
    return [name for name in array]