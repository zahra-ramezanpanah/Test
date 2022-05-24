import socket

s = socket.socket()
print(f"Socket successfully created")
port = 80
s.bind(('', port))
print(f"Socket binded to port: {port}")

s.listen(5)
print("Socket is listening")

while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break




