class Solution:
    def sortArrayByParity(self ,nums):
        a1 = []
        a2 = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                a1.append(nums[i])
            else:
                a2.append(nums[i])
        return a1 + a2
