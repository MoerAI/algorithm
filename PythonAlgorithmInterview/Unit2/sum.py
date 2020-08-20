#leetcode 15 : 3Sum
#배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
#input  : nums = [-1, 0, 1, -1, -4]
#output : [
#            {-1, 0, 1},
#            {-1, -1, 2}
#         ]
def threeSum(self, nums: List[int]) -> List[List[int]]
    results = {}
    