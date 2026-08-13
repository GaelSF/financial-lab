import numpy as np
import matplotlib.pyplot as plt

def future_value(pv, rate, periods):
    fv = pv*(1+rate)**periods
    return fv

def present_value(fv, rate, periods):
    pv = fv/(1+rate)**periods
    return pv

print(future_value(50000, 0.1, 10))

real = (1+0.1)/(1+0.04) - 1.0
print(real)

fv_real = 50000*(1+real)**10

print(fv_real)


def p_a(rn, infla, d0, n ):
    pa = d0*((1+rn)/(1+infla))**n
    return pa


print('Poder adquisitivo A:', p_a(0.1, 0.02, 10000, 5))
print('Poder adquisitivo B:', p_a(0.15, 0.12, 10000, 5))
