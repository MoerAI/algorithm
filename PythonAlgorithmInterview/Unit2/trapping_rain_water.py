#leetcode 43 : Trapping Rain Water
#높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
#이미지가 있는 문제임

#1. 브루트 포스로 계산하기
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    height_max = height[0]
    for i in height:
        height_max = max(height[i], height_max)
        volume += height_max - height[i]
            
#2. 투 포인터를 이용
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
        
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
        
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
        if left_max<=right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

#3. 스택 쌓기