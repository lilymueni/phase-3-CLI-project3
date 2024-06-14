from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

from models.equipment import Equipment
from models.maintenance_record import MaintenanceRecord
from models.technician import Technician

def main():
    # Main loop to display menu and handle user choices
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_equipment()
        elif choice == "2":
            list_all_equipment()
        elif choice == "3":
            delete_equipment()
        elif choice == "4":
            find_equipment_by_id()
        elif choice == "5":
            add_maintenance_record()
        elif choice == "6":
            list_all_maintenance_records()
        elif choice == "7":
            delete_maintenance_record()
        elif choice == "8":
            find_maintenance_record_by_id()
        elif choice == "9":
            add_technician()
        elif choice == "10":
            list_all_technicians()
        elif choice == "11":
            delete_technician()
        elif choice == "12":
            find_technician_by_id()
        else:
            print(Fore.RED + "Invalid choice")

def menu():
    # Display the menu options with colored output
    print(Style.BRIGHT + Fore.YELLOW + "Please select an option:")
    print(Fore.CYAN + "0. Exit the program")
    print(Fore.CYAN + "1. Add Equipment")
    print(Fore.CYAN + "2. List All Equipment")
    print(Fore.CYAN + "3. Delete Equipment")
    print(Fore.CYAN + "4. Find Equipment by ID")
    print(Fore.CYAN + "5. Add Maintenance Record")
    print(Fore.CYAN + "6. List All Maintenance Records")
    print(Fore.CYAN + "7. Delete Maintenance Record")
    print(Fore.CYAN + "8. Find Maintenance Record by ID")
    print(Fore.CYAN + "9. Add Technician")
    print(Fore.CYAN + "10. List All Technicians")
    print(Fore.CYAN + "11. Delete Technician")
    print(Fore.CYAN + "12. Find Technician by ID")

def add_equipment():
    # Add a new equipment to the database
    name = input("Enter equipment name: ")
    type = input("Enter equipment type: ")
    serial_number = input("Enter equipment serial number: ")
    Equipment.create(name, type, serial_number)
    print(Fore.GREEN + "Equipment added successfully.")

def list_all_equipment():
    # List all equipment from the database
    equipments = Equipment.get_all()
    for equipment in equipments:
        print(Fore.BLUE + f"ID: {equipment.id}, Name: {equipment.name}, Type: {equipment.type}, Serial Number: {equipment.serial_number}")

def delete_equipment():
    # Delete equipment from the database
    equipment_id = int(input("Enter equipment ID to delete: "))
    Equipment.delete(equipment_id)
    print(Fore.GREEN + "Equipment deleted successfully.")

def find_equipment_by_id():
    # Find equipment by ID
    equipment_id = int(input("Enter equipment ID: "))
    equipment = Equipment.find_by_id(equipment_id)
    if equipment:
        print(Fore.BLUE + f"ID: {equipment.id}, Name: {equipment.name}, Type: {equipment.type}, Serial Number: {equipment.serial_number}")
    else:
        print(Fore.RED + "Equipment not found.")

def add_maintenance_record():
    # Add a maintenance record to the database
    equipment_id = int(input("Enter equipment ID: "))
    maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")
    description = input("Enter description of work performed: ")
    performed_by = input("Enter name of person who performed maintenance: ")
    MaintenanceRecord.create(equipment_id, maintenance_date, description, performed_by)
    print(Fore.GREEN + "Maintenance record added successfully.")

def list_all_maintenance_records():
    # List all maintenance records from the database
    records = MaintenanceRecord.get_all()
    for record in records:
        print(Fore.BLUE + f"ID: {record.id}, Equipment ID: {record.equipment_id}, Date: {record.maintenance_date}, Description: {record.description}, Performed by: {record.performed_by}")

def delete_maintenance_record():
    # Delete a maintenance record from the database
    record_id = int(input("Enter maintenance record ID to delete: "))
    MaintenanceRecord.delete(record_id)
    print(Fore.GREEN + "Maintenance record deleted successfully.")

def find_maintenance_record_by_id():
    # Find a maintenance record by ID
    record_id = int(input("Enter maintenance record ID: "))
    record = MaintenanceRecord.find_by_id(record_id)
    if record:
        print(Fore.BLUE + f"ID: {record.id}, Equipment ID: {record.equipment_id}, Date: {record.maintenance_date}, Description: {record.description}, Performed by: {record.performed_by}")
    else:
        print(Fore.RED + "Maintenance record not found.")

def add_technician():
    # Add a technician to the database
    name = input("Enter technician name: ")
    specialization = input("Enter technician specialization: ")
    contact_info = input("Enter technician contact info: ")
    Technician.create(name, specialization, contact_info)
    print(Fore.GREEN + "Technician added successfully.")

def list_all_technicians():
    # List all technicians from the database
    technicians = Technician.get_all()
    for technician in technicians:
        print(Fore.BLUE + f"ID: {technician.id}, Name: {technician.name}, Specialization: {technician.specialization}, Contact Info: {technician.contact_info}")

def delete_technician():
    # Delete a technician from the database
    technician_id = int(input("Enter technician ID to delete: "))
    Technician.delete(technician_id)
    print(Fore.GREEN + "Technician deleted successfully.")

def find_technician_by_id():
    # Find a technician by ID
    technician_id = int(input("Enter technician ID: "))
    technician = Technician.find_by_id(technician_id)
    if technician:
        print(Fore.BLUE + f"ID: {technician.id}, Name: {technician.name}, Specialization: {technician.specialization}, Contact Info: {technician.contact_info}")
    else:
        print(Fore.RED + "Technician not found.")

def exit_program():
    # Exit the program
    print(Fore.YELLOW + "Goodbye!")
    exit()

if __name__ == "__main__":
    main()
