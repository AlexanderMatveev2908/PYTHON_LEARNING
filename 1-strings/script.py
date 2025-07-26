import re

print('AAA'.lower())
print('bbb'.upper())

print('a b c d'.title())


print(re.sub(r'\b33\b', '4', '1 2 33 5'))

print(len('Lorem ipsum dolor sit amet \
          consectetur adipisicing elit. \
          Vero, enim quidem. Vitae \
          mollitia earum, doloremque \
          ipsum consequatur pariatur, \
          inventore recusandae eos ad \
          deleniti repellendus ullam. \
          Rem, enim cum. Numquam, velit.' * 2))

print((' ' * 10).strip() + 'abc...')

print(('monkey'.title().center(20, ' ').lstrip()).center(30, '='))

print('coffee'.ljust(16, '.'))
print('juice'.rjust(8, '.'))

print('abc'[1:])

print('content...'.startswith('cont'))
print('content...'.endswith('...'))