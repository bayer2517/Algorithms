class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowest_number = 0
        highest_number = len(nums) - 1
        
        
        while lowest_number <= highest_number:
            mid = lowest_number + (highest_number-lowest_number)//2
            if nums[mid] > target:
                highest_number = mid-1
            elif nums[mid] < target:
                lowest_number = mid + 1
            else:
                return mid
            
        return -1
        
