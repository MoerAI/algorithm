# leetcoe 347 : Top K Frequent Elements
# k번 이상 등장하는 요소를 추출하라.
# input  : nums = [1,1,1,2,2,3], k = 2
# output : [1,2]

import collections
import heapq
from typing import List

#Counter를 이용한 음수 순 추출
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

