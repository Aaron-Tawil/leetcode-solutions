import glob
import re
import unicodedata

def clean_title(raw):
    # Normalize UTF characters and fix dashes
    raw = unicodedata.normalize("NFKD", raw)
    raw = raw.replace("–", "-").replace("—", "-")
    # Capitalize words
    return raw.strip().title()

files = sorted(
    [f for f in glob.glob("*.py") if not f.startswith("update_readme")],
    key=lambda f: int(f.split("-", 1)[0])
)

lines = [
    "# LeetCode Solutions\n",
    "| # | Title | Diff. | Link |",
    "|---|-------|-------|------|",
]

for fn in files:
    text = open(fn, encoding="utf-8").read()
    meta = dict(re.findall(r"#\s*(\w+):\s*(.+)", text))
    num, slug = fn.split("-", 1)
    slug_base = slug.rsplit(".", 1)[0]

    title = meta.get("Problem") or slug_base.replace("-", " ")
    title = clean_title(title)

    diff = meta.get("Difficulty", "")
    link = meta.get("Link", f"https://leetcode.com/problems/{slug_base}/")
    
    lines.append(f"| {num} | {title} | {diff} | [Link]({link}) |")

open("README.md", "w", encoding="utf-8").write("\n".join(lines))
