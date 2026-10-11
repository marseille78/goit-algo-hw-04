def all_phones(contacts: dict) -> None:

    for user, phone in contacts.items():
        print(f"{user}: {phone}")