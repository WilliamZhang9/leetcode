from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty or has one element, return its length
        if len(nums) < 2:
            return len(nums)
        
        # Initialize a pointer for the position of the next unique element
        insert_pos = 1
        
        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous element
            if nums[i] != nums[i - 1]:
                # Place it at the insert position index
                nums[insert_pos] = nums[i]
                # Move the insert position forward
                insert_pos += 1
        
        # Return the position index as the count of unique elements
        return insert_pos
