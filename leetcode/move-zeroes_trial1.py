class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = []

        for i in range(len(nums)):
            if nums[i] == 0:
                holder.append(i)
            elif nums[i] != 0 and len(holder) >= 1:
                first = holder.pop(0)
                nums[first], nums[i] = nums[i], nums[first]
                holder.append(i)
        return nums