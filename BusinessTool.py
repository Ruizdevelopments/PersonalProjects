def pos():
    print("\n=== POS (Point of Sale) ===")
    item = input("Enter item name: ")
    try:
        price = float(input("Enter price: $"))
        quantity = int(input("Enter quantity: "))
        total = price * quantity
        result = f"POS - Item: {item}, Price: ${price:.2f}, Quantity: {quantity}, Total: ${total:.2f}"
        print(result + "\n")
        export_to_txt(result)
    except ValueError:
        print("Invalid input. Please enter numeric values for price and quantity.\n")

def crm():
    print("\n=== CRM (Customer Management) ===")
    name = input("Customer name: ")
    service = input("Service provided (e.g., haircut, oil change): ")
    contact = input("Contact info: ")
    result = f"CRM - Name: {name}, Service: {service}, Contact: {contact}"
    print(result + "\n")
    export_to_txt(result)

def scheduler():
    print("\n=== Scheduling Platform ===")
    name = input("Client name: ")
    date = input("Appointment date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    result = f"Scheduler - Client: {name}, Date: {date}, Time: {time}"
    print(result + "\n")
    export_to_txt(result)

def inventory():
    print("\n=== Inventory/Sales Tracker ===")
    product = input("Product name: ")
    try:
        stock = int(input("Units in stock: "))
        sold = int(input("Units sold today: "))
        remaining = stock - sold
        result = f"Inventory - Product: {product}, Stock: {stock}, Sold: {sold}, Remaining: {remaining}"
        print(result + "\n")
        export_to_txt(result)
    except ValueError:
        print("Invalid input. Please enter numeric values for stock and sold.\n")

def invoice():
    print("\n=== Quoting/Invoice Generator ===")
    client = input("Client name: ")
    service = input("Service or product: ")
    try:
        amount = float(input("Amount to charge: $"))
        result = f"--- INVOICE ---\nClient: {client}\nItem: {service}\nTotal Due: ${amount:.2f}"
        print(result + "\n")
        export_to_txt(result)
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.\n")

def export_to_txt(data):
    try:
        with open("business_output.txt", "a") as file:
            file.write(data + "\n")
    except IOError:
        print("Error: Unable to write to file.\n")

def main():
    while True:
        print("Select a tool:")
        print("1. POS")
        print("2. CRM")
        print("3. Scheduling")
        print("4. Inventory/Sales Tracker")
        print("5. Quoting/Invoice Generator")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")
        if choice == '1':
            pos()
        elif choice == '2':
            crm()
        elif choice == '3':
            scheduler()
        elif choice == '4':
            inventory()
        elif choice == '5':
            invoice()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()

