from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_len = len(set(nums))
        list_len = len(nums)
        if set_len == list_len:
            return False
        else:
            return True


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = Solution().containsDuplicate(nums)
    print(res)
