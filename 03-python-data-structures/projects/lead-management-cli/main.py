import leads

def show_menu():
    print()
    print("=" * 50)
    print("              LEAD MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Lead")
    print("2. View All Leads")
    print("3. Search Leads")
    print("4. Update Lead Status")
    print("5. Delete Lead")
    print("6. Calculate Pipeline Value")
    print("7. Filter by Country")
    print("8. Filter by Status")
    print("9. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-9): ")
        
        if choice == '1':
            leads.add_lead()
        elif choice == '2':
            leads.view_all_leads()
        elif choice == '3':
            leads.search_leads()
        elif choice == '4':
            leads.update_lead_status()
        elif choice == '5':
            leads.delete_lead()
        elif choice == '6':
            leads.calculate_pipeline_value()
        elif choice == '7':
            leads.filter_by_country()
        elif choice == '8':
            leads.filter_by_status()
        elif choice == '9':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()