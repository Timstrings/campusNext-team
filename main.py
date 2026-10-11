from campusflow.tickets import (
    create_ticket,
    generate_ticket_id,
    view_ticket
)

tickets = []

ticket1 = create_ticket(
    "Internet not working",
    "Network",
    "high",
    12,
    generate_ticket_id(tickets)
)

tickets.append(ticket1)

ticket2 = create_ticket(
    "Computer not working",
    "Hardware",
    "medium",
    2,
    generate_ticket_id(tickets)
)

tickets.append(ticket2)

result = view_ticket(tickets, "T002")

print(result)