import os
import shutil

# 내장 템플릿 파일 목록 (예: README, .gitignore 등)
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "builtin_templates")

def list_templates():
    files = [f for f in os.listdir(TEMPLATE_DIR) if os.path.isfile(os.path.join(TEMPLATE_DIR, f))]
    for idx, fname in enumerate(files, 1):
        print(f"{idx}. {fname}")
    return files

def select_templates():
    files = list_templates()
    selected = set()
    print("Enter the template file number(s) to add (separate multiple with commas, press Enter to cancel):")
    nums = input("> ").replace(" ", "")
    if not nums:
        return []
    for n in nums.split(","):
        try:
            idx = int(n) - 1
            if 0 <= idx < len(files):
                selected.add(files[idx])
        except Exception:
            pass
    return list(selected)

def add_templates(target_dir, selected_templates):
    for fname in selected_templates:
        src = os.path.join(TEMPLATE_DIR, fname)
        dst = os.path.join(target_dir, fname)
        if not os.path.exists(dst):
            shutil.copyfile(src, dst)
