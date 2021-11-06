from datetime import datetime
from libsx.initTerminal import add, div, helloWorld, kill, quad, quadMax, subAdd
import getpass
import platform
import re 

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
        add_list= [float(s) for s in re.findall(r'-?\d+\.?\d*', Text)]
        _valx = add_list[0]
        _valy = add_list[1]
        c = add(_valx, _valy)
    if (Text == "subAdd()"):
        add_list= [float(s) for s in re.findall(r'-?\d+\.?\d*', Text)]
        _valx = add_list[0]
        _valy = add_list[1]
        d = subAdd(_valx, _valy)
    if (Text == "quad()"):
        add_list= [float(s) for s in re.findall(r'-?\d+\.?\d*', Text)]
        _valx = add_list[0]
        _valy = add_list[1]
        e = quad(_valx, _valy)
    if (Text == "div()"):
        add_list= [float(s) for s in re.findall(r'-?\d+\.?\d*', Text)]
        _valx = add_list[0]
        _valy = add_list[1]
        f = div(_valx, _valy)
    if (Text == "quadMax()"):
        add_list= [float(s) for s in re.findall(r'-?\d+\.?\d*', Text)]
        _valx = add_list[0]
        _valy = add_list[1]
        g = quadMax(_valx, _valy)                             


