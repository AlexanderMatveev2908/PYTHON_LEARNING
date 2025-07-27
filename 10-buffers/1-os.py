import os
import base64
from pathlib import Path

p = os.getcwd()
# print(p)


def to_MB(v: int):
    return round(v / (1024 ** 2), 2)


dirname = os.path.dirname(p)
# basename = os.path.basename(p)
# filename, ext = os.path.splitext(basename)

# print(dirname)
# print(basename)
# print(filename)
# print(ext)

my_file = os.path.join(p, 'script.py')
# print(my_file)
bsn = os.path.basename(my_file)
# print(bsn)
# print(os.path.splitext(bsn))

with open(my_file, 'rb') as f:
    # data = f.read().decode(encoding='utf-8')
    # data = f.read().hex()
    data = base64.b64encode(f.read())
    print(data)

os.makedirs(os.path.join(p, 'test'), exist_ok=True)

Path('1.txt').touch(exist_ok=True)

# 'w' = write (overwrite if exists)
# 'a' = append (add at the end)
# 'x' = exclusive create (crashes if it exists)

with open('2.txt', 'w') as f:
    f.write(' Some content \n' * 10)

cwd = Path.cwd()
long_f = cwd / '2.txt'
print(long_f.is_file())
print(long_f.is_dir())

bs = long_f.stat().st_size
print(bs)


print(to_MB(bs))
