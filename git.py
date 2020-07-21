import subprocess


def get_current_branch():
    '''return the current branch'''
    process = subprocess.Popen(["git", "rev-parse", "--abbrev-ref", "HEAD", "--"],
                               shell=False, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    out_text = str(output).replace("b'", "").replace("'", "").split("\\n")
    out_text = [l.split("\\t") for l in out_text]
    current_branch = out_text[0][0]
    return current_branch


def get_staged_files():
    '''return a list of current staged files for this commit'''
    process = subprocess.Popen(["git", "diff", "--cached", "--name-status"],
                               shell=False, stdout=subprocess.PIPE)

    output = process.communicate()[0]
    out_text = str(output).replace("b'", "").replace("'", "").split("\\n")
    out_text = [l.split("\\t") for l in out_text]

    return out_text
