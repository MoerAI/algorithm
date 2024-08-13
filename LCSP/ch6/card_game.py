# https://dmoj.ca/problem/ccc99s1
# 카드 한벌로 플레이 하는 간단한 2인 게임의 점수를 기록 하는 프로 그램
# 전체 카드는 52장이고, 13개의 카드 중 점수가 높은 카드는 4개
# jack, Queen, King, Ace가 "높은 카드"
# 플레이어 A가 먼저 카드를 뒤집음
# 플레이어 B가 다음 카드를 뒤집음
# 데크가 소진될 때까지 A와 B가 번갈아 가며 카드를 뒤집음
# ace -> 최소 4장 뒤집 어야 하는 카드 남음. 남은 카드는 하이 카드, 4점 획득
# king -> 최소 3장 뒤집어 야 할 카드 남음. 다음 카드는 없음. 3장의 카드는 높은 카드. 3점 획득
# queen -> 최소 2장 뒤집어 야 할 카드 남음. 다음 카드 없음. 2장의 카드는 높은 카드. 2점 획득
# jack -> 최소 1장 뒤집어 야 할 카드 남음. 다음 카드 없음.  다음 카드가 높은 카드가 아닐 경우. 1점 득점
# 입력 52줄 각 카드는 소문자이고 순서대로 뒤집음
# 출력은 각 플레 이어의 최종 점수
# Player A: n point(s).
# Player B: m point(s).

NUM_CARDS = 52

# 높은 카드가 리스트에 포함되어 있는지 확인
def no_high(lst):
    high_card = ['jack', 'queen', 'king', 'ace']
    for h in high_card:
        if h in lst:
            return True
    return False

deck = []

# 카드의 순서를 받음
for i in range(NUM_CARDS):
    deck.append(input())

score_a = 0
score_b = 0
player = 'A'

# 카드에 따른 플레이어의 점수를 계산
for i in range(NUM_CARDS):
    card = deck[i]
    points = 0
    remaining = NUM_CARDS - i - 1

    if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points  = 1
    elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')