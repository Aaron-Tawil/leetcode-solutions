import os
import json
import shutil
import re
import glob

def get_problem_data(json_path):
    """Reads the leetcode_questions.json file and returns a dictionary 
       mapping problem ID to its metadata."""
    with open(json_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    problem_data = {}
    for q_obj in questions:
        question = q_obj.get('data', {}).get('question', {})
        if question:
            front_id = question.get('questionFrontendId')
            title = question.get('title')
            difficulty = question.get('difficulty')
            tags = [tag['name'] for tag in question.get('topicTags', [])]
            url = question.get('url')
            
            if all([front_id, title, difficulty, tags, url]):
                problem_data[front_id] = {
                    'title': title,
                    'difficulty': difficulty,
                    'tags': tags,
                    'url': url
                }
    return problem_data

def organize_files(problem_data):
    """Organizes solution files into difficulty/topic folders."""
    files_to_process = [f for f in os.listdir('.') if f.endswith('.py') and re.match(r'^\d+', f)]
    
    if not files_to_process:
        print("No new solution files found to organize.")
        return

    for file in files_to_process:
        match = re.match(r'(\d+)', file)
        if match:
            problem_id = match.group(1)
            if problem_id in problem_data:
                info = problem_data[problem_id]
                difficulty = info['difficulty']
                tags = info['tags']
                
                if not tags:
                    print(f"No tags found for {file}, skipping organization.")
                    continue

                print(f"Organizing {file}...")
                
                for tag in tags:
                    tag_folder_name = tag.replace(' ', '_').replace('-', '_')
                    
                    if not os.path.exists(difficulty):
                        os.makedirs(difficulty)
                        
                    topic_path = os.path.join(difficulty, tag_folder_name)
                    if not os.path.exists(topic_path):
                        os.makedirs(topic_path)
                    
                    destination = os.path.join(topic_path, file)
                    shutil.copy(file, destination)
                    print(f"  - Copied to {destination}")
                
                os.remove(file)
                print(f"  - Removed original file: {file}\n")
            else:
                print(f"Could not find data for problem ID {problem_id} from file {file}")

def update_readme(problem_data):
    """Updates the README.md file with all solutions."""
    print("Updating README.md...")
    
    # Find all solution files in the subdirectories
    all_solution_files = []
    for difficulty in ['Easy', 'Medium', 'Hard']:
        if os.path.exists(difficulty):
            for root, _, files in os.walk(difficulty):
                for file in files:
                    if file.endswith('.py'):
                        all_solution_files.append(os.path.join(root, file))

    # Use a set to store unique problem numbers to avoid duplicates in README
    processed_problems = set()
    readme_lines = [
        "# LeetCode Solutions",
        "| # | Title | Diff. | Tags | Solution |",
        "|---|-------|-------|------|----------|",
    ]

    # Sort files based on problem number
    sorted_files = sorted(all_solution_files, key=lambda f: int(re.match(r'(\d+)', os.path.basename(f)).group(1)))

    for file_path in sorted_files:
        file_name = os.path.basename(file_path)
        match = re.match(r'(\d+)', file_name)
        if match:
            problem_id = match.group(1)
            if problem_id not in processed_problems:
                if problem_id in problem_data:
                    info = problem_data[problem_id]
                    title = f"[{info['title']}]({info['url']})"
                    diff = info['difficulty']
                    tags = ", ".join(info['tags'])
                    solution_link = f"[Solution]({file_path.replace(os.path.sep, '/')})"
                    readme_lines.append(f"| {problem_id} | {title} | {diff} | {tags} | {solution_link} |")
                    processed_problems.add(problem_id)
                else:
                    print(f"Warning: Could not find data for problem number {problem_id}.")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(readme_lines))
    
    print("README.md updated successfully.")

def main():
    json_path = 'leetcode_questions.json'
    if not os.path.exists(json_path):
        print(f"Error: '{json_path}' not found.")
        return
        
    problem_data = get_problem_data(json_path)
    
    # First, organize any new files in the root directory
    organize_files(problem_data)
    
    # Then, update the README with all solution files
    update_readme(problem_data)
    
    print("\nScript finished.")

if __name__ == "__main__":
    main()
