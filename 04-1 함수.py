Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle as t
t.shape('tiger')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    t.shape('tiger')
  File "<string>", line 8, in shape
  File "C:\Dev211\Python\Python3\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named tiger
t.shape('fish')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shape('fish')
  File "<string>", line 8, in shape
  File "C:\Dev211\Python\Python3\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named fish
t.shape('turtle')
t.forward(100)
t.up(100)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t.up(100)
TypeError: up() takes 0 positional arguments but 1 was given
t.back(100)
t.right(200)
t.left(500)
t.forward(100)
t.right()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.right()
TypeError: right() missing 1 required positional argument: 'angle'
TypeError: right() missing 1 required positional argument: 'angle'
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t.right
<function right at 0x0000014420A01C60>
<function right at 0x0000014420A01C60>t
KeyboardInterrupt
t.right(100)
t.right(100)
t.right(100)
t.left(20)
t.left(10)
t.left(5)
t.left(5)
t.forward(100)
t.right(100)
t.right(100)
t.forward(100)
t.forward(100)
clear
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
KeyboardInterrupt
t.clear()
t.shape()
'turtle'
t.shape('turtle')
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
t.shape('turtle')
for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(5):
    t.forward(100)
    t.right(108)

t.clear
<function clear at 0x0000014420A004C0>
t.clear()
for i in range(4):
    t.forward(100)
    t.right(108)

for i in range(4):
    t.forward(100)
    t.right(72)

for i in range(5):
    t.forward(100)
    t.right(360/5)

t.clear()

for i in range(10):
    t.forward(100)
    t.right(360/10)

