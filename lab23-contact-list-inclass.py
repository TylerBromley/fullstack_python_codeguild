# lab23-contact-list-inclass.py

def load(path):
    with open(path) as f:
        lines = f.read().split('\n')

    contacts = []
    header = lines[0].split(",")
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(header, row))
        contacts.append(contact)
    return contacts

def save(contacts, path, header):
    lines = [",".join(header)]
    for contact in contacts:
        row = ",".join(contact.values())
        lines.append(row)
    csv = "\n".join(lines)
    with open(path, 'w') as f:
        f.write(csv)

def print_contact(contact):
    if type(contact) is str:
        print(contact)
    else:
        for k,v in contact.items():
            print(f"{k}: {v}")

def print_all_contacts(contacts):
    for contact in contacts:
        print_contact(contact)
        print()

def find_contact(contacts, name):
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            return i
    return -1

def create(contacts, contact):
    contacts.append(contact)
    return contact

def read(contacts, name):
    idx = find_contact(contacts, name)
    if idx > -1:
        return contacts[idx]
    else:
        return f"{name} not in contact list"

def update(contacts, name, updated_info):
    idx = find_contact(contacts, name)
    if idx > -1:
        contacts[idx].update(updated_info)
        return contacts[idx]
    else:
        return f"{name} not in contact list"

def delete(contacts, name):
    idx = find_contact(contacts, name)
    if idx > -1:
        return contacts.pop(idx)
    else:
        return f"{name} not in contact list"

def list_commands():
    pass

def main():
    path = "contacts.csv"
    contacts = load(path)
    valid_inputs = ['h', 'help',
                    'co', 'commands',
                    'c', 'create',
                    'r', 'read',
                    'u', 'update', 
                    'd', 'delete',
                    'l', 'list'
    ]

    while True:
        while True:
            command = input("What operations would you like to perform: ")
            if command in valid_inputs:
                break
            list_commands()

        if command in ['h', 'help', 'commands']:
            list_commands()
        elif command in ['x', 'exit']:
            break

        elif command.startswith('c'):
            contact = {}
            for key in header:
                value = input(f"{key}: ")
                contact[key] = value
            print("Creating contact...")
            create(contacts, contact)

        elif command.startswith('r'):
            name = input("Name: ")
            print(read(contacts, name))

        elif command.startswith('u'):
            contact = {}
            for key in header:
                value = input(f"{key}: ")
                contact[key] = value
            contact = {k:v for k, v in contact.items() if v}
            print("Updating contact...")
            update(contacts, contact["name"], contact)

        elif command.startswith('d'):
            name = input("Name: ")
            print(f"Deleting {name}...")
            print_contact(delete(contacts, name))

        elif command.startswith('l'):
            print_all_contacts(contacts)

        elif command in ['e', 'exit']:
            save(contacts, path, header)
            break

main()
