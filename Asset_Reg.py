# Sample data
assets = [
    {"ID": 1, "Name": "Laptop", "Category": "Hardware", "Owner": "Alice"},
    {"ID": 2, "Name": "Mouse", "Category": "Hardware", "Owner": "Bob"},
    {"ID": 3, "Name": "Antivirus Software", "Category": "Software", "Owner": "Carol"}
]

def display_assets(assets):
    print("\nCurrent IT Assets:")
    for asset in assets:
        print(f"ID: {asset['ID']}, Name: {asset['Name']}, Category: {asset['Category']}, Owner: {asset['Owner']}")
    print()

def display_menu():
    print("Menu:")
    print("1. Amend a record")
    print("2. Add a record")
    print("3. Delete a record")
    print("4. Display full details of a selected record")
    print("5. Exit")

def amend_record(assets):
    id_to_amend = int(input("Enter the ID of the record you want to amend: "))
    for asset in assets:
        if asset["ID"] == id_to_amend:
            asset["Name"] = input("Enter new Name: ")
            asset["Category"] = input("Enter new Category: ")
            asset["Owner"] = input("Enter new Owner: ")
            print("Record amended successfully.")
            return
    print("Record not found.")

def add_record(assets):
    new_id = int(input("Enter new ID: "))
    new_name = input("Enter new Name: ")
    new_category = input("Enter new Category: ")
    new_owner = input("Enter new Owner: ")
    assets.append({"ID": new_id, "Name": new_name, "Category": new_category, "Owner": new_owner})
    print("Record added successfully.")

def delete_record(assets):
    id_to_delete = int(input("Enter the ID of the record you want to delete: "))
    for asset in assets:
        if asset["ID"] == id_to_delete:
            assets.remove(asset)
            print("Record deleted successfully.")
            return
    print("Record not found.")

def display_full_details(assets):
    id_to_display = int(input("Enter the ID of the record you want to display: "))
    for asset in assets:
        if asset["ID"] == id_to_display:
            print(f"Full details of record ID {id_to_display}:")
            print(f"Name: {asset['Name']}")
            print(f"Category: {asset['Category']}")
            print(f"Owner: {asset['Owner']}")
            return
    print("Record not found.")

def main():
    while True:
        display_assets(assets)
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            amend_record(assets)
        elif choice == "2":
            add_record(assets)
        elif choice == "3":
            delete_record(assets)
        elif choice == "4":
            display_full_details(assets)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()