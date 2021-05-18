from database import fetch_entries, add_entry, create_table

menu = """Please select one of the following options:
1. Add new entry for today
2. View entries
3. Exit

Your Input: """

Welcome = """Welcome to the programming diary"""


def prompt_new_entry():
    date = input("Enter a date:")
    content = input("Enter the content:")
    add_entry(date, content)


def view_entries(entries):
    for entry in entries:
        print(f"Date : {entry[1]}\nContent : {entry[0]}\n\n")


print(Welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
        print("***Entry added***")
    elif user_input == "2":
        entries = fetch_entries()
        view_entries(entries)
    else:
        print("Invalid input, Please try again!")
