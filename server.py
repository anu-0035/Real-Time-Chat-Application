import socket
import threading

HOST = "127.0.0.1"
PORT = 1202 # use any port from 0 - 65535
LISTENER_LIMIT = 5
active_client = [] # list for currently connected user to server

# func for listing for upcoming message from client
def listen_for_messages(client, username):

    while 1:
        message = client.recv(2048).decode('utf-8')
        if message :
            fin_message = username + ":~ " + message
            send_message_to_all(fin_message)
        else:
            print(f"The message sent from client{username} is empty")

# func to send message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())


# func to sent message to all the client who are connected to server
def send_message_to_all(message):
    for user in active_client:
        send_message_to_client(user[1], message)
        

# func to handle the client
def client_handler(client):
    #server will listen for client message that have
    # conatins the username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != "":
            active_client.append((username,client))
            prompt_message = "SERVER:~ " + f"{username} added to the chat"
            send_message_to_all(prompt_message)
            break
        else:
            print("Client username is empty")
            
    threading.Thread(target = listen_for_messages, args = (client,username,)).start()

# main function
def main():
    #socket class object
    #AF_NET: we are using IPV4 address
    #SOCK_STREAM: for TCP protocol and for UDP use SOCK_DGRAM
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        server.bind((HOST,PORT))
        print(f"Running the server on HOST: {HOST} AND PORT: {PORT}")
    except:
        print(f"Unable to bind to HOST: {HOST} and PORT: {PORT}")
    #set sever limit
    server.listen(LISTENER_LIMIT)

    # This while will keep listening to all the client connections
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to  client {address[0]} {address[1]}")

        threading.Thread(target = client_handler, args = (client,) ).start()

    
    
if __name__ == "__main__":
    main()


