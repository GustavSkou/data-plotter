from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x = Symbol("x")
function = 2*x**2

f = function
f_mark = f.diff(x)
F = f.integrate(x)

f = lambdify(x, f)
f_mark = lambdify(x, f_mark)
F = lambdify(x, F)

f_str = str(f(x))
f_mark_str = str(f_mark(x))
F_str = str(F(x))

print(f_str.replace("**", "^"))
print(f_mark_str.replace("**", "^"))
print(F_str.replace("**", "^"))

x_value = np.linspace(-30, 30, 100)

f_xpoints = x_value
F_xpoints = x_value
f_mark_xpoints = x_value

f_ypoints = []
F_ypoints = []
f_mark_ypoints = []

n=0
for n in range(100):
    f_ypoints.append(f(x_value[n]))
    F_ypoints.append(F(x_value[n]))
    f_mark_ypoints.append(f_mark(x_value[n]))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

f_graf, = plt.plot(f_xpoints, f_ypoints, label="f(x)")
#F_graf, = plt.plot(F_xpoints, F_ypoints, label="F(x)")
f_mark_graf, = plt.plot(f_mark_xpoints, f_mark_ypoints, label="f'(x)")

leg = plt.legend(loc='upper left')

plt.show()