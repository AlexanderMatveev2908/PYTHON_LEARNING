my_tpl = tuple(('Apple', 'Pear'))


print(my_tpl)
print(isinstance(my_tpl, tuple))

my_tpl_2 = tuple((*my_tpl, 'Cherry'))
print(my_tpl_2)

my_tpl_3 = (1, 2, 3)

print(isinstance(my_tpl_3, tuple))
