#leetcode 561 : Array Partition 1
#n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
#input  : nums = [1, 4, 3, 2]
#output : 4

#오름차순으로 정렬 한 후 계산
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum
