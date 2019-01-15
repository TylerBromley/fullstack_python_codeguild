# lab23-contact-list.py

def create(username, contacts, keys):
    user_row = []
    user_row.append(username)
    user_row.append(input("Please enter your favorite fruit: "))
    user_row.append(input("Please enter your favorite color: "))
    user_row = dict(zip(keys, user_row))
    contacts.append(user_row)
    return contacts

def read(username, contacts):
    for i in contacts:
        if i.get("name") == username:
            return i

def update(username, contacts):
    for i in contacts:
        if i["name"] == username:
            attribute = input("Please enter the attribute you'd like to change: ")
            new_value = input("Please enter the new value: ")
            if i.get(attribute):
                i[attribute] = new_value
            return i

def delete(username, contacts):
    for i in contacts:
        if i.get("name") == username:
            contacts.remove(i)
    return contacts

def main():
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')

    keys = lines[0]
    keys = keys.split(',')
    rows = lines[1:]

    contacts = []
    for row in rows:
        row = row.split(',')
        row = dict(zip(keys, row))
        contacts.append(row)

    while True:
        username = input("Please enter the name or type 'quit': ").strip().capitalize()
        if username == "Quit":
            break
        else:
            crud = input("Would you like to [c]reate, [r]ead, [u]pdate or [d]elete: ").lower()
            if crud[0] == "c":
                print(create(username, contacts, keys))
            elif crud[0] == "r":
                print(read(username, contacts))
            elif crud[0] == "u":
                print(update(username, contacts))
            elif crud[0] == "d":
                print(delete(username, contacts))
            else:
                print("invalid user input.")
            columns = []
            first_line = list(contacts[0].keys())
            columns.append(",".join([str(x) for x in first_line]))
            for i in range(len(contacts)):
                csv_values = list(contacts[i].values())
                columns.append(",".join([str(x) for x in csv_values]))
            for i in range(len(columns)):
                print(columns[i])

            with open('contacts.csv', 'w') as f:
                for i in range(len(columns)):
                    if i == len(columns)-1:
                        f.write(columns[i])
                    else:
                        f.write(columns[i] + "\n")

main()
