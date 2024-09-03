**UDP Client-Server Messaging System**

**Project Overview**

This project implements a simple UDP (User Datagram Protocol) client-server application designed to facilitate message exchange between multiple clients on a local network. The server listens for incoming messages on a specified port and broadcasts messages to all connected clients. Clients can send messages and view messages sent by others, with the system ensuring that clients do not see their own messages in the list.

**Key Features**

- **Broadcast Communication:** Uses UDP broadcasting to send messages to all clients in the local network.
- **Concurrency:** Utilizes threading to handle incoming messages concurrently with other operations, allowing seamless message sending and receiving.
- **Message Filtering:** Ensures that clients do not see their own messages in the received list.
- **User Interaction:** Provides a simple interface for clients to send messages and view received messages.

**How It Works**

1. **Server Setup:**
   - The server is configured to listen on port `5051`.
   - It uses a broadcast IP (`192.X.X.255`) to send messages to all clients in the network.
   - The server handles UDP packets, which are connectionless and ideal for broadcasting.

2. **Client Initialization:**
   - Each client is prompted to input their first and last name, which is used to identify the client.
   - The client name is used to filter out the client’s own messages from the list of received messages.

3. **Message Handling:**
   - **Receiving Messages:**
     - The server continuously listens for incoming messages in a separate thread.
     - Messages are decoded, logged, and displayed with the sender’s information and timestamp.
   - **Sending Messages:**
     - Clients can enter messages which are then sent to the server and broadcasted to the network.
     - Messages are formatted with the sender’s first name, last name, and message content.

4. **Displaying Messages:**
   - Clients can list all received messages.
   - Messages are listed with a unique index, and clients can view details of specific messages by selecting the corresponding index.
