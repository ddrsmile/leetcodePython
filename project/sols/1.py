class Solution(object):
  def twoSum(self, nums, target):
    tmp = {}
    for i, n in enumerate(nums):
      if target - n in tmp:
        return tmp[target - n] + 1, i + 1
      else:
        tmp[n] = i
