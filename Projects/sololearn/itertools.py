from itertools import accumulate, takewhile, product, permutations

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

a={1,2}
print(len(list(product(range(3), a))))