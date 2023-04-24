def tally(nums: list[int]) -> int:
  total = 0
  for num in nums:
     # Record each value of total and num at the end of the loop body.
     total = total + num
  return total
result = tally([4, 9, 2, 1])
