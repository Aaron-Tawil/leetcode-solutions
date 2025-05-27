import glob
import re

files = sorted(glob.glob("*.py"), key=lambda f: int(f.split("-",1)[0]))
lines = [
    "# LeetCode Solutions\n",
    "| # | Title | Diff. | Link |",
    "|---|-------|-------|------|",
]
for fn in files:
    text = open(fn).read()
    meta = dict(re.findall(r"#\s*(\w+):\s*(.+)", text))
    num, slug = fn.split("-",1)
    title = meta.get("Problem", slug.rsplit(".",1)[0].replace("-", " ").title())
    diff  = meta.get("Difficulty", "")
    link  = meta.get("Link", f"https://leetcode.com/problems/{slug.rsplit('.',1)[0]}/")
    lines.append(f"| {num} | {title} | {diff} | [Link]({link}) |")

open("README.md","w", encoding="utf-8").write("\n".join(lines))
