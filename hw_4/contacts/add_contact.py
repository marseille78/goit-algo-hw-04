def add_contact(args: list, contacts: dict) -> str:

    if len(args) != 2:
        return "Command 'add' must have 2 arguments: 'add username phone'"

    name, phone = args

    if name in contacts:
        return f"User {name} already exists"

    contacts[name] = phone

    return "Contact added"