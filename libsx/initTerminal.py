import time 
def helloWorld():
    return print("HELLO WORLD!")
def kill():
    return print("Terminating execution...."), time.sleep(3), quit()
def add(_valx, _valy):
    return print (_valx + _valy)
def subAdd(_valx, _valy):
    return print (_valx - _valy)
def quad(_valx, _valy):
    return print (_valx * _valy)
def div(_valx, _valy):
    return print (_valx / _valy)
def quadMax(_valx, _valxx):
    return print(_valx ** _valxx)
