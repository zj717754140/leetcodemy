
class Solution:
    def addTwoNumbers(self, nums, target):
        for i, data in enumerate(nums):
            # a = target - data
            # if a in nums:
            #    if i != nums.index(a):
            #        return [i, nums.index(a)]
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

a = [2,7,11,15]
target = 9
solu = Solution()
print(solu.addTwoNumbers(a,target))
