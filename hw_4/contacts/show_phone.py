def show_phone(args: list, contacts: dict) -> str:

    if len(args) != 1:
        print("Command 'phone' must have 1 arguments: 'phone username'")

    name = args[0]

    if name in contacts:
        return f"{name}: {contacts[name]}"

    return "Unknown username"