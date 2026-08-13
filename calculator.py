d0 = 1e4
r = 0.08
t = 5
dt = d0*((1+r)**t)
print(dt)
print(dt-d0)
print(100*(dt-d0)/d0)


dc = 20000
r2 = 0.07
t2 = 5

d_0 = dc/((1+r2)**t2)
d_2 = dc/((1+0.12)**t2)
print(d_0)
print(d_2)

