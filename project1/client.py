import socket


def math(x, y, op):
  if op == '+':
    return int(x) + int(y)
  if op == '-':
    return int(x) - int(y)
  if op == '*':
    return int(x) * int(y)
  if op == '/':
    return int(x) / int(y)
  else:
    raise 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("login.ccs.neu.edu", 27993))

message = 'cs3700spring2016 HELLO 000500067\n'
status = 'STATUS'
sock.send(message)

while status != 'BYE':
  response = sock.recv(256)
  words = response.split()
  status = words[1]

  if status == 'STATUS':
    answer = math(words[2], words[4], words[3])
    message = 'cs3700spring2016 ' + str(answer) + '\n'

  sock.send(message)

flag = words[2]

print flag