### Asset database

class ITAsset:
    def __init__(self, record_number, item_name, imie_number, asset_type, colour, assigned_user_name, assigned_user_department, date_issued):
        self.record_number = record_number
        self.item_name = item_name
        self.imie_number = imie_number
        self.asset_type = asset_type
        self.colour = colour
        self.assigned_user_name = assigned_user_name
        self.assigned_user_department = assigned_user_department
        self.date_issued = date_issued

    def display(self):
        print(f"{self.record_number}\t{self.item_name}\t{self.imie_number}\t{self.asset_type}\t{self.colour}\t{self.assigned_user_name}\t{self.assigned_user_department}\t{self.date_issued}")

## adds in a sperator

def display_assets(assets):
    print("Record Number\tItem Name\tIMIE Number\tAsset Type\tColour\tAssigned User Name\tAssigned User Department\tDate Issued")
    print("-" * 250)
    for asset in assets:
        asset.display()

def find_asset_by_record_number(assets, record_number):
    for asset in assets:
        if asset.record_number == record_number:
            return asset
    return None

## making sure the IMIE number is a number

def get_valid_imie():
    while True:
        try:
            imie_number = int(input("Enter IMIE number: "))
            return imie_number
        except ValueError:
            print("Invalid IMIE number. Please enter a valid number.")

## date entry

def get_valid_date():
    while True:
        date_str = input("Enter date issued (DD.MM.YYYY): ")
        if len(date_str) != 10 or date_str[2] != '.' or date_str[5] != '.':
            print("Invalid date format. Please enter the date in DD.MM.YYYY format.")
            continue
        day, month, year = date_str.split('.')
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("Invalid date format. Please enter the date in DD.MM.YYYY format.")
            continue
        day, month, year = int(day), int(month), int(year)
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return date_str
        else:
            print("Invalid date values. Please enter the date in DD.MM.YYYY format.")


def main():
    # Asset register sample data table
    assets = [
        ITAsset(1, "Laptop", "1234567890", "Computer", "Black", "Alice", "HR", "10.10.2023"),
        ITAsset(2, "Desktop", "0987654321", "Computer", "White", "Bob", "IT", "01.01.2024"),
        ITAsset(3, "Printer", "1112131415", "Hardware", "Grey", "Charlie", "Finance", "28.09.2023"),
        ITAsset(4, "Router", "1617181920", "Networking", "Black", "David", "IT", "28.04.2020"),
        ITAsset(5, "Monitor", "2122232425", "Hardware", "Black", "Eve", "HR", "02.02.2012"),
        ITAsset(6, "Keyboard", "2627282930", "Hardware", "Black", "Frank", "Admin", "04.04.2008"),
        ITAsset(7, "Mouse", "3132333435", "Hardware", "Black", "Grace", "Admin", "07.07.2021"),
        ITAsset(8, "Phone", "3637383940", "Mobile Telephone", "Silver", "Hank", "Sales", "15.04.2022"),
        ITAsset(9, "Tablet", "4142434445", "Computer", "Gold", "Ivy", "Marketing", "10.10.2018"),
        ITAsset(10, "Switch", "4647484950", "Networking", "Blue", "Jack", "IT", "09.06.2021")
    ]

    display_assets(assets)
    
    while True:
        print("\nMenu:")
        print("1. Amend a record")
        print("2. Add a record")
        print("3. Delete a record")
        print("4. Display full details of a selected record")
        print("5. Show all records")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            record_number = int(input("Enter the record number to amend: "))
            asset = find_asset_by_record_number(assets, record_number)
            if asset:
                print("Current details:")
                asset.display()
                asset.item_name = input("Enter new item name: ")
                asset.imie_number = get_valid_imie()
                asset.asset_type = input("Enter new asset type: ")
                asset.colour = input("Enter new colour: ")
                asset.assigned_user_name = input("Enter new assigned user name: ")
                asset.assigned_user_department = input("Enter new assigned user department: ")
                asset.date_issued = get_valid_date()
                print("Record updated.")
            else:
                print("Record not found.")
        
        elif choice == '2':
            record_number = len(assets) + 1
            item_name = input("Enter item name: ")
            imie_number = get_valid_imie()
            asset_type = input("Enter asset type: ")
            colour = input("Enter colour: ")
            assigned_user_name = input("Enter assigned user name: ")
            assigned_user_department = input("Enter assigned user department: ")
            date_issued = get_valid_date()
            new_asset = ITAsset(record_number, item_name, imie_number, asset_type, colour, assigned_user_name, assigned_user_department, date_issued)
            assets.append(new_asset)
            print("Record added.")
        
        elif choice == '3':
            record_number = int(input("Enter the record number to delete: "))
            asset = find_asset_by_record_number(assets, record_number)
            if asset:
                assets.remove(asset)
                print("Record deleted.")
            else:
                print("Record not found.")
        
        elif choice == '4':
            record_number = int(input("Enter the record number to display: "))
            asset = find_asset_by_record_number(assets, record_number)
            if asset:
                print("Full details of the record:")
                asset.display()
            else:
                print("Record not found.")

        elif choice == '5':
            display_assets(assets)
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()