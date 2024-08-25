# Real-Time-Chat-Application
It is a GUI based application allows users to communicate instantly through text messages over the internet. 

Here's a basic algorithm for the real-time chat server application:

1. **Initialize the Server:**
   - Create a socket using the TCP protocol (`SOCK_STREAM`).
   - Bind the server to a specific IP address (`HOST`) and port (`PORT`).
   - Set the server to listen for incoming connections with a defined listener limit.

2. **Accept Client Connections:**
   - Enter an infinite loop where the server waits for incoming client connections.
   - When a client connects, accept the connection and start a new thread to handle communication with that client.

3. **Handle Client Communication:**
   - **Username Registration:**
     - In the client-handling thread, receive the client's username.
     - Add the client and their username to the list of active clients.
     - Broadcast a message to all connected clients, notifying them of the new user's entry into the chat.
   - **Message Listening:**
     - Continuously listen for messages from the client.
     - When a message is received, format it with the sender's username.
     - Broadcast the formatted message to all connected clients.

4. **Broadcast Messages:**
   - Implement a function that sends a message to all active clients.
   - Iterate through the list of active clients and send the message to each client.

5. **Error Handling and Edge Cases:**
   - Handle cases where the received message or username is empty.
   - Ensure the server doesn't crash due to unexpected inputs or connection drops.

6. **Continue Listening:**
   - Keep the server running indefinitely, accepting new clients and handling messages as they arrive.

This algorithm outlines the core workflow of the server, focusing on connection handling, message broadcasting, and basic error management.
