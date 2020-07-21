import re
import os


def create_markdown_empty_file(root, file):
    [open(md_path, "a") for md_path in markdown_on_folder_on_root(root, file)]


def join_markdown_top_title(root, file):
    is_first_md = True
    joined_text = []
    for md_path in markdown_on_folder_on_root(root, file):
        with open(md_path, "r+") as f:
            start = False
            for line in f.readlines():
                is_big_title = line[0] == "#" and line[1] == " "

                if is_first_md or (start and not is_big_title):
                    is_first_md = False
                    joined_text.append(line)

                if is_big_title:
                    start = not start

                if not start:
                    break
    with open(os.path.join(root, f"joined_{file}"), "w") as joined:
        joined.writelines(joined_text)


def folder_on_root(root):
    return [os.path.join(root, folder)
            for folder in os.listdir(root) if os.path.isdir(folder)]


def markdown_on_folder_on_root(root, file):
    return [os.path.join(folder, file) for folder in folder_on_root(root)]


def add_new_version_on_markdown(root, file, new_version_text):
    for md_path in markdown_on_folder_on_root(root, file):
        with open(md_path, "r+") as f:
            lines = f.readlines()
            f.seek(0)
            f.write(f"# {new_version_text}\n")
            f.writelines(lines)


create_markdown_empty_file(".", "email.md")
add_new_version_on_markdown(".", "email.md", "MasterTool 3.30 Beta 04")
create_markdown_empty_file(".", "release_notes.md")
join_markdown_top_title(".", "email.md")
