import socket
import sys
import json

HOST, PORT = "localhost", 9999

"""
sends the images to the server when asked
sends commands to the robot when server says so
"""

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    data = "Hi"
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
    print received
finally:
    sock.close()

