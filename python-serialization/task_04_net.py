#!/usr/bin/env python3

import socket
import json

def start_server():
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific port
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Accept a connection
        connection, client_address = server_socket.accept()

        try:
            # Receive the serialized data
            data = connection.recv(1024)

            if data:
                # Deserialize the data
                received_dict = json.loads(data)

                # Print the received dictionary
                print('Received Dictionary from Client:')
                print(received_dict)
        finally:
            # Close the connection
            connection.close()

def send_data(data_dict):
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    try:
        # Serialize the dictionary
        serialized_data = json.dumps(data_dict)

        # Send the serialized data to the server
        client_socket.sendall(serialized_data.encode())
    finally:
        # Close the connection
        client_socket.close()

def main():
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Give server some time to start listening
    time.sleep(1)

    # Run the client to send data
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }
    send_data(sample_dict)

    # Ensure server thread ends
    server_thread.join()

if __name__ == "__main__":
    main()
