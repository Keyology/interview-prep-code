class Solution:
    def twoSum(self, nums, target):
        """
        -----------------VARIABLE TABEL--------------------------
        nums: [2, 7, 11, 15]
        target:9
        h: {2:0, 7:1},
        n:2
        i:1
        return [0,1]

        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]