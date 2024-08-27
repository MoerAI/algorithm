def count_special_pairs(cities):
    city_count = {}
    
    for city, state in cities:
        key = city[:2] + state
        if key not in city_count:
            city_count[key] = 0
        city_count[key] += 1
    
    total_pairs = 0
    
    for city, state in cities:
        city_prefix = city[:2]
        state_prefix = state
        normal_key = city_prefix + state_prefix
        reversed_key = state_prefix + city_prefix
        
        if normal_key != reversed_key and reversed_key in city_count:
            total_pairs += city_count[reversed_key]
    
    return total_pairs // 2

cities = [
    ("MIAMI", "FL"),
    ("DALLAS", "TX"),
    ("FLINT", "MI"),
    ("CLEMSON", "SC"),
    ("BOSTON", "MA"),
    ("ORLANDO", "FL")
]

print(count_special_pairs(cities))
