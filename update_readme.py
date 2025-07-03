import glob
import re
import json

# Load the LeetCode questions data from the JSON file
try:
    with open("leetcode_questions.json", "r", encoding="utf-8") as f:
        all_problems_data = json.load(f)
    # Create a dictionary for faster lookups by questionFrontendId
    problems_dict = {
        item['data']['question']['questionFrontendId']: item['data']['question']
        for item in all_problems_data if item.get('data') and item['data'].get('question')
    }
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading or parsing leetcode_questions.json: {e}")
    problems_dict = {}

def get_problem_details(problem_number):
    return problems_dict.get(str(problem_number))

files = sorted(
    [f for f in glob.glob("*.py") if re.match(r"^\d", f)],
    key=lambda f: int(f.split("-", 1)[0])
)

lines = [
    "# LeetCode Solutions\n",
    "| # | Title | Diff. | Tags |",
    "|---|-------|-------|------|",
]

for fn in files:
    num = fn.split("-", 1)[0]
    problem_data = get_problem_details(num)

    if not problem_data:
        print(f"Warning: Could not find data for problem number {num}. Using filename as fallback.")
        slug_base = fn.split("-", 1)[1].rsplit(".", 1)[0]
        title = f"{slug_base.replace('-', ' ').title()}"
        diff = "N/A"
        tags = "N/A"
        link = f"https://leetcode.com/problems/{slug_base}/"
        title = f"[{title}]({link})"
    else:
        # Extract all data from the JSON
        title = problem_data.get('title', 'N/A')
        diff = problem_data.get('difficulty', 'N/A')
        tags = ", ".join(tag['name'] for tag in problem_data.get('topicTags', [])) or "N/A"
        link = problem_data.get('url', '#')
        title = f"[{title}]({link})"

    lines.append(f"| {num} | {title} | {diff} | {tags} |")

open("README.md", "w", encoding="utf-8").write("\n".join(lines))

print("README.md updated successfully. All data is now sourced from the JSON file.")
