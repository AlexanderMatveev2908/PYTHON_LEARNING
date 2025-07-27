from pathlib import Path
import shutil

cwd = Path.cwd()

p = Path("2.txt")
if p.exists() and p.is_file():
    p.unlink()

if (cwd / '5').exists():
    shutil.rmtree('5')
