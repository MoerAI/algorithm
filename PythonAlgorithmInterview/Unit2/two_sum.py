#leetcode 1 : Two Sum
#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
#input  : nums = [2, 7, 11, 15]
#output : [0, 1]

#1. Brute-Force
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
#2. in을 이용한 탐색
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)
        
#3. 첫 번째 수를 뺀 결과 키 조회
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    #키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i 
        
    #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i !=nums_map[target - num]:
            return nums.index(num), nums_map[target - num]

