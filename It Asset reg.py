class ITAsset:
    def __init__(self, record_number, item_name, imie_number, asset_type, colour, assigned_user_name, assigned_user_department, po_order_number):
        self.record_number = record_number
        self.item_name = item_name
        self.imie_number = imie_number
        self.asset_type = asset_type
        self.colour = colour
        self.assigned_user_name = assigned_user_name
        self.assigned_user_department = assigned_user_department
        self.po_order_number = po_order_number

    def display(self):
        print(f"{self.record_number}\t{self.item_name}\t{self.imie_number}\t{self.asset_type}\t{self.colour}\t{self.assigned_user_name}\t{self.assigned_user_department}\t{self.po_order_number}")

## adds in a sperator

def display_assets(assets):
    print("Record Number\tItem Name\tIMIE Number\tAsset Type\tColour\tAssigned User Name\tAssigned User Department\tPO Order Number")
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
            print("Invalid IMIE number. Please enter a valid integer.")

def main():
    # Sample data
    assets = [
        ITAsset(1, "Laptop", "1234567890", "Computer", "Black", "Alice", "HR", "PO001"),
        ITAsset(2, "Desktop", "0987654321", "Computer", "White", "Bob", "IT", "PO002"),
        ITAsset(3, "Printer", "1112131415", "Hardware", "Grey", "Charlie", "Finance", "PO003"),
        ITAsset(4, "Router", "1617181920", "Networking", "Black", "David", "IT", "PO004"),
        ITAsset(5, "Monitor", "2122232425", "Hardware", "Black", "Eve", "HR", "PO005"),
        ITAsset(6, "Keyboard", "2627282930", "Hardware", "Black", "Frank", "Admin", "PO006"),
        ITAsset(7, "Mouse", "3132333435", "Hardware", "Black", "Grace", "Admin", "PO007"),
        ITAsset(8, "Phone", "3637383940", "Mobile Telephone", "Silver", "Hank", "Sales", "PO008"),
        ITAsset(9, "Tablet", "4142434445", "Computer", "Gold", "Ivy", "Marketing", "PO009"),
        ITAsset(10, "Switch", "4647484950", "Networking", "Blue", "Jack", "IT", "PO010")
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
                asset.po_order_number = input("Enter new PO order number: ")
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
            po_order_number = input("Enter PO order number: ")
            new_asset = ITAsset(record_number, item_name, imie_number, asset_type, colour, assigned_user_name, assigned_user_department, po_order_number)
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