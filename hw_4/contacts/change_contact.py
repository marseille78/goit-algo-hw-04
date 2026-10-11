def change_contact(args: list, contacts: dict) -> str:

    if len(args) != 2:
        return "Command 'change' must have 2 arguments: 'change username phone'"

    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Phone was changed"

    return "You've entered unknown username"