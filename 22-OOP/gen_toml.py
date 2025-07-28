from pathlib import Path
from tomlkit import parse, dumps, document, table


conf_p = Path("pyproject.toml")

if not conf_p.exists():
    print("📄 No pyproject.toml found, creating new one...")
    doc = document()
else:
    print("📄 Found existing pyproject.toml, updating...")
    doc = parse(conf_p.read_text())

tool_table = doc.setdefault("tool", table())
black_table = tool_table.setdefault("black", table())

black_table["line-length"] = 79
black_table["target-version"] = ["py312"]

conf_p.write_text(dumps(doc))
print("✅ [tool.black] section configured.")
