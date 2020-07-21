import os


def create_markdown_empty_file(root, file):
    for md_path in markdown_on_git_folder_on_root(root, file):
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        open(md_path, "a")


def remove_markdown_file(root, file):
    for md_path in markdown_on_git_folder_on_root(root, file):
        os.remove(md_path)


def join_markdown_top_title(root, file):
    is_first_md = True
    joined_text = []
    for md_path in markdown_on_git_folder_on_root(root, file):
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


def git_folder_on_root(root):
    for folder in os.listdir(root):
        dir_path = os.path.join(root, folder)
        if os.path.isdir(dir_path) and os.listdir(dir_path).__contains__(".git"):
            yield dir_path


def markdown_on_git_folder_on_root(root, file):
    for folder in git_folder_on_root(root):
        yield os.path.join(folder, file)


def add_new_version_on_markdown(root, file, new_version_text):
    for md_path in markdown_on_git_folder_on_root(root, file):
        with open(md_path, "r+") as f:
            lines = f.readlines()
            f.seek(0)
            f.write(f"# {new_version_text}\n")
            f.writelines(lines)


if __name__ == "__main__":
    root = "..\\.."
    email_md = "Version Notes\\email.md"
    release_md = "Version Notes\\release_notes.md"
    
    # Create new Markdown files
    create_markdown_empty_file(root, email_md)
    create_markdown_empty_file(root, release_md)

    # # Remove Markdown files
    # remove_markdown_file(root, email_md)
    # remove_markdown_file(root, release_md)

    # Add new version title tag on markdown
    add_new_version_on_markdown(root, email_md, "MasterTool 3.30 Beta 05")
    add_new_version_on_markdown(root, release_md, "MasterTool 3.30 Beta 05")

    # # Write joined_file.md with latest changes
    # join_markdown_top_title(root, email_md)
    # join_markdown_top_title(root, release_md)
