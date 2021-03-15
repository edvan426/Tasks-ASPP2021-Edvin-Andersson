import simple_math as sm
import pytest
import numpy as np

#testing numbers between -50 and 50
a,b,a0,a1,a2,x=(np.random.random(6)-0.5)*100
print (a,b,a0,a1,a2,x)

def test_simple_add():
    assert sm.simple_add(a,b) == a+b

def test_simple_sub():
    assert sm.simple_sub(a,b) == a-b

def test_simple_mult():
    assert sm.simple_mult(a,b) == a*b

def test_simple_div():
    assert sm.simple_div(a,b) == a/b

def test_poly_first():
    assert sm.poly_first(x,a0,a1) == a0 + a1*x

def test_poly_second():
    assert sm.poly_second(x,a0,a1,a2) == a0 + a1*x +a2*(x**2)
