def ordinal(n):
    return "%d%s" % (n, "th" if 4 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    num_datasets = int(data[index])
    index += 1
    results = []
    
    for dataset in range(1, num_datasets + 1):
        n, k = map(int, data[index].split())
        index += 1
        
        word_count = {}
        for _ in range(n):
            word = data[index].strip()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            index += 1
        
        sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
        frequencies = sorted(set(word_count.values()), reverse=True)
        
        if k <= len(frequencies):
            target_freq = frequencies[k-1]
            most_common_words = [word for word, count in sorted_words if count == target_freq]
        else:
            most_common_words = []
        
        results.append(f"{ordinal(k)} most common word(s):")
        if most_common_words:
            results.extend(most_common_words)
        results.append("")
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()