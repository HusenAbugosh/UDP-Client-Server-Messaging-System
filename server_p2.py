import socket
import datetime
import threading

# Server settings:
server_port = 5051
buffer_size = 1024
broadcast_ip = '192.X.X.255'

# to get and save the user names :
client_name = None
if client_name is None:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    client_name = f"{first_name} {last_name}"

clients = {}  # <--this a  Dictionary to keep track of client addresses and last messages
received_messages = []  # <--  a list to store the messages

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # <-- to  creates a UDP socket.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # <-- to allow broadcasting.
server_socket.bind(('', server_port))  # <-- to binds the socket to the specified port.

print("UDP Server listening on port", server_port)


#Prints a list of received messages, excluding messages from the client itself.
def display_received_messages():
    if received_messages:
        print("\nList of received messages:")
        for idx, (sender, time, msg) in enumerate(received_messages, start=1):
            if sender != client_name:
                print(f"-{idx} received a message from {sender} at {time}")
    else:
        print("\nNo messages to display.")


def rec():
    # Receive message from any client
    message, client_address = server_socket.recvfrom(buffer_size)
    decoded_message = message.decode()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update client's last message and timestamp
    sender_info = decoded_message.split(';')
    if len(sender_info) == 3:
        sender = f"{sender_info[0]} {sender_info[1]}"
        if client_name != sender:
            print(f"\nReceived message from {sender} at {current_time}")
        received_messages.append((sender, current_time, sender_info[2]))
        rec()

# creating a new thread to run the rec function, allowing the server to receive messages concurrently with other tasks:
t1 = threading.Thread(target=rec)
t1.start()


#to show the options menu:
while True:

    print("\nOptions:\n1. Send another message\n2. Show all messages")
    option = input("Select an option (1/2): ")

    if option == '1':

        message = input("Enter your message: ")
        send_message = f"{first_name};{last_name};{message}"
        server_socket.sendto(send_message.encode(), (broadcast_ip, server_port)) #<-- to send it via UDP to the broadcast address.

    elif option == '2':
        display_received_messages()
        choice = input("Enter line number followed by 'D' to display the message (e.g., 1D): ")
        if choice.endswith('D') and choice[:-1].isdigit():
            index = int(choice[:-1]) - 1
            if 0 <= index < len(received_messages):
                print(
                    f"Message from {received_messages[index][0]} at {received_messages[index][1]}: {received_messages[index][2]}")
            else:
                print("Invalid line number.")
    else:
        print("Invalid option. Please select 1 or 2.")
