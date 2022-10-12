from inspect import stack
from stack import Stack

s = Stack(999)
s.put("$")
s.put("A")
s.put("0")
for e in s.list:
  print(e)
print(s.list)