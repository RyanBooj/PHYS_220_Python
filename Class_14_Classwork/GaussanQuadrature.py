from gaussxw import gaussxw

N=3
a=0
b=2

def f(x):
    return x**4 -2*x + 1

x, w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

s = 0.0
for k in range(N):
    s += wp[k]*f(xp[k])

print(s)
