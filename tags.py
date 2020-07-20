email_hashtag = {"group": "email",
                 "tag": "#email",
                 "required_files": ["email_OVERRIDEWITHBRANCHNAME.md"],
                 "cannot_coexist": ["#no_email"]}

no_email_hashtag = {"group": "email",
                    "tag": "#no_email",
                    "required_files": [],
                    "cannot_coexist": ["#email", "#release_notes"]}

release_notes_hashtag = {"group": "release_notes",
                         "tag": "#release_notes",
                         # OVERRIDEWITHBRANCHNAME see methods:
                         # replace_placeholder_value() and required_files_modified_and_staged()
                         "required_files": ["release_notes_OVERRIDEWITHBRANCHNAME.md"], 
                         "cannot_coexist": ["#no_release_notes", "#no_email"]}

no_release_notes_hashtag = {"group": "release_notes",
                            "tag": "#no_release_notes",
                            "required_files": [],
                            "cannot_coexist": ["#release_notes"]}

def all_hashtags():
    return [email_hashtag, no_email_hashtag,
                release_notes_hashtag, no_release_notes_hashtag]