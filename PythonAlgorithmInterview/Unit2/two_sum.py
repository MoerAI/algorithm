#leetcode 1 : Two Sum
#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
#input  : nums = [2, 7, 11, 15]
#output : [0, 1]

#1. Brute-Force
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + num[j] == target:
                return [i, j]
            
#2. in을 이용한 탐색
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)