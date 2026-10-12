def all_phones(contacts: dict) -> list:

    all_users = []

    for user, phone in contacts.items():
        all_users.append(f"{user}: {phone}")

    return all_users