class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):  # Corrected this line
            if nums[right] != 0:
                # swapping
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # move the left pointer to the right

# Time: O(n) --> Linear time to traverse the array once
# Space: O(1) --> Constant space as we're modifying the array in-place
