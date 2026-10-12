from campusflow.tickets import create_ticket, generate_ticket_id, list_tickets, view_ticket
from campusflow.workflow import assign_ticket, update_status, reopen_ticket, get_ticket_queue
from campusflow.reports import generate_report
from campusflow.storage import load_tickets, save_tickets


def main():
    try:
        tickets = load_tickets()
    except (ValueError, OSError) as error:
        print("Unable to load saved tickets:", error)
        print("Existing data was not overwritten.")
        return
    actions = {
        "1": "Create Ticket", "2": "List Tickets", "3": "View Ticket",
        "4": "Assign Ticket", "5": "Update Status", "6": "Reopen Ticket",
        "7": "Ticket Queue", "8": "Generate Report", "9": "Exit",
    }
    while True:
        print("\n=== CAMPUSFLOW ===")
        for key, label in actions.items():
            print(f"{key}. {label}")
        try:
            choice = input("Choose 1-9: ").strip()
            if choice == "9":
                print("Goodbye!")
                break
            if choice not in actions:
                print("Invalid choice.")
                continue
            if choice == "1":
                title = input("Title: ")
                category = input("Category (Network/Hardware/Software/Other): ")
                urgency = input("Urgency (low/medium/high): ")
                users = int(input("Affected users: "))
                ticket = create_ticket(title, category, urgency, users, generate_ticket_id(tickets))
                tickets.append(ticket)
                save_tickets(tickets)
                print("Ticket created successfully!", ticket)
            elif choice == "2":
                print(list_tickets(tickets) or "No tickets available.")
            elif choice == "3":
                ticket_id = input("Ticket ID: ").strip()
                print(view_ticket(tickets, ticket_id) or "Ticket not found.")
            elif choice == "4":
                ticket_id = input("Ticket ID: ").strip()
                name = input("Staff name: ")
                updated = assign_ticket(tickets, ticket_id, name)
                save_tickets(tickets)
                print("Assigned:", updated)
            elif choice == "5":
                ticket_id = input("Ticket ID: ").strip()
                status = input("Status (open/in_progress/resolved): ").strip().lower()
                updated = update_status(tickets, ticket_id, status)
                save_tickets(tickets)
                print("Updated:", updated)
            elif choice == "6":
                updated = reopen_ticket(tickets, input("Ticket ID: ").strip())
                save_tickets(tickets)
                print("Reopened:", updated)
            elif choice == "7":
                print(get_ticket_queue(tickets) or "No unresolved tickets.")
            elif choice == "8":
                print("Report:", generate_report(tickets))
        except (ValueError, OSError) as error:
            print("Error:", error)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
