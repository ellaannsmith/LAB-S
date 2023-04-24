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

