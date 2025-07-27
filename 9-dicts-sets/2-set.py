nums = {x for x in range(5)}

print(isinstance(nums, set))

print(-1 in nums)

nums_2 = {x + 5 for x in range(5)}
nums_2.update({2, 3})

print(nums)
print(nums_2)

c = nums.intersection(nums_2)
print(c)

d = nums.difference(nums_2)
print(d)
