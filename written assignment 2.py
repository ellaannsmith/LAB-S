def tally(nums: list[int]) -> int:
  total = 0
  for num in nums:
     # Record each value of total and num at the end of the loop body.
     total = total + num
  return total


def copy(nums: list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list

def increment_all(nums: list[int]) -> list[int]:
  new_list = []
  for value in nums:
     new_list.append(value + 1)
  return new_list


result = increment_all([4, 9, 2, 1])
