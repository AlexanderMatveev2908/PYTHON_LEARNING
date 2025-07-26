import re

REG_INT = re.compile(r'^\d+$')
REG_FLOAT = re.compile(r'^\d?\.\d{1,2}$')  # noqa: E231
