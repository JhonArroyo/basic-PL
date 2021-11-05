from datetime import datetime
from libsx.initTerminal import add, div, helloWorld, kill, quad, quadMax, subAdd
import getpass
import platform

username = getpass.getuser()
print("Compiling Prototype v0.1")
print("Username: "+ username)
print("OS: "+ platform.platform())
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Time: " + dt_string)

while True:  
    Text = input(">>")
    if (Text == "helloworld()"):
        a = helloWorld()
    if (Text == "kill()"):
        b = kill()
    if (Text == "add()"):
        b = add()
    if (Text == "subAdd()"):
        b = subAdd()
    if (Text == "quad()"):
        b = quad()
    if (Text == "div()"):
        b = div()
    if (Text == "quadMax()"):
        b = quadMax()                                
