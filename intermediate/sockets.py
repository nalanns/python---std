import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55556))
s.listen()
while True:
    client, adress = s.accept()
    print(f"Connection from {adress} has been established!")
    client.send("You are connected".encode())
    client.close()  # Close the client connection after sending the message



 