# List, in order, the values that x takes at each step.
more = [x + 1 for x in [1,2,3,4]]
print() # What is the value of more at this point?
def square(n: int) -> int:
   return n * n
squares = [square(x) for x in [1, 2, 3, 4]]
print()

def check(n: int) -> bool:
  return n > 2
answer = [x for x in range(5) if check(x)]
print()

def inc(m: int) -> int:
  return m + 1
def check(n: int) -> bool:
    return n > 2
answer = [inc(x) for x in range(5) if check(x)]
print()

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
