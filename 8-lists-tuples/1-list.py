clr_arg = ['red', 'green', 'blue']

for i, clr in enumerate(clr_arg):
    clr_arg[i] = clr.title()

print(clr_arg)

my_set = set()
my_list = []

for i in range(10):
    for j in range(2):
        my_set.add(i)
        my_list.append(i)


my_set.update([20, 40])

my_set.remove(0)
# discard does not throw err
my_set.discard(60)

print(my_list)
print(my_set)
