#!/usr/bin/env python
# --------------------------------------------------
# Miguel Riem Oliveira.
# PARI, September 2020.
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time

import dog_lib

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23457)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# Create an instance of class Dog
dog = dog_lib.Dog('Bobi', 'Brown', 3)
dog.addBrother('Lassie')
dog.addBrother('Tobin')
print(dog)

# serialize dog instance
messages = dog.name + ',' + str(dog.age) + ',' + str(dog.color)
for brother in dog.brothers:
    messages += ',' + brother

print(messages)

while True:
    message_formated = str(messages).encode("utf-8")
    print("Sending message_formated: " + message_formated)
    sock.sendall(message_formated)
    time.sleep(2)  # wait for two seconds

sock.close()  # close connection
