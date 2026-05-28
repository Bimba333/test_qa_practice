def is_valid_email(email):
    if isinstance(email, str) and email.count("@") == 1 and email.split("@")[0] != '' and "." in email.split("@")[1]:
        return True
    return False