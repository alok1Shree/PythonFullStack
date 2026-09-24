# Customer Support Ticket Queue - FIFO Management System

ticket_queue = ['Ticket_001', 'Ticket_002', 'Ticket_003', 'Ticket_004', 'Ticket_005']
ticket_queue.append('Ticket_006')  # Adding a new ticket to the queue
print("Current Ticket Queue:", ticket_queue)

current_ticket = ticket_queue.pop(0)  # Processing the first ticket in the queue
print("Processing:", current_ticket)
print("Updated Ticket Queue:", ticket_queue)