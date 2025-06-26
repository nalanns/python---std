import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55556))  # Connect to the server at the specified address and port
message = s.recv(1024)  # Receive data from the server (up to 1024 bytes)
s.close()  # Close the socket connection
print(message.decode())  # Decode the received bytes to a string and print it
# Output the received message
# Output: "You are connected" if the server is running and sends this message
# Note: Ensure the server is running before executing this client code.
# If the server is not running, this code will raise an error.


 