#leetcode 49 : Group Anagrams
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

#input  : ["eat", "tea", "ate", "nat", "bat"]
#output : [
#            ["ate", "eat", "tea"],
#            ["nat", "tan"],
#            ["bat"]
#          ]

def groupAnagrams(self, strs: List[srt]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()