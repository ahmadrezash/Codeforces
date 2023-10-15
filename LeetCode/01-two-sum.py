from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = nums
        sorted_nums = sorted(sorted_nums)
        le = len(sorted_nums)
        i = 0
        j = le - 1
        while True:
            num1 = sorted_nums[i]
            num2 = sorted_nums[j]
            if num1 + num2 == target:
                break
            elif num1 + num2 <= target:
                i += 1
            elif num1 + num2 >= target:
                j -= 1
            if i == j:
                break
        if num1 == num2:
            i1 = nums.index(num1)
            nums.pop(i1)
            i2 = nums.index(num2) + 1
            res = [i1, i2]
        else:
            res = [nums.index(num1), nums.index(num2)]
        res.sort()
        return res


if __name__ == "__main__":
    nums = [1, 3, 3, 2, 4, 5]
    target = 9
    # nums = [3, 3]
    # target = 6
    nums = [-1, -2, -3, -4, -5]
    target = -8
    a = Solution().twoSum(nums=nums, target=target)
    print(a)
