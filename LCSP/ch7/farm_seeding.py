def read_cows(input_file, num_cows):
    """
    소의 수와 소의 정보가 있는 파일을 읽고
    각 소가 좋아하는 목초지 리스트 반환
    """
    favorites = []
    for i in range(num_cows):
        lst = input_file.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favorites.append(lst)
    return favorites


def cows_with_favorite(favorites, pasture):
    """
    각 소가 좋아하는 목초지 리스트와 목초지 번호를 받고
    현재 목초지를 좋아하는 소들의 리스트 반환    
    """
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)
    return cows


def types_used(favorites, cows, pasture_types):
    """
    각 소가 좋아한는 목초지 리스트, 현재 목초지를 좋아하는 소들의 리스트, 각 목초지에 대해 선택된 풀 유형을 받고
    소가 좋아하는 목초지를 기반으로 이미 사용된 풀 유형의 리스트 반환
    """
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used


def smallest_available(used):
    """
    사용된 풀리스트를 받아서
    사용되지 않은 가장 작은 번호의 풀 유형을 반환
    """
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type


def write_pastures(output_file, pasture_types):
    """
    목초지에 심을 풀들의 유형이 정수로 담긴 리스트를 받아서
    output_file에 write
    """
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')


# main
input_file = open('revegetate.in','r')
output_file = open('revegetate.out','w')

lst = input_file.readline().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favorites = read_cows(input_file, num_cows)

pasture_types = [0]

for i in range(1, num_pastures + 1):
    cows = cows_with_favorite(favorites, i)
    eliminated = types_used(favorites, cows, pasture_types)
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_types)

pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()