from sympy import *
import matplotlib.pyplot as plt
import numpy as np

info_listen = []

x = Symbol("x")
function = x**2+x

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


x_akse_info = [-4, 4, 1000]

x_akse = np.linspace(x_akse_info[0], x_akse_info[1], x_akse_info[2])

f_xpoints = x_akse
F_xpoints = x_akse
f_mark_xpoints = x_akse

f_ypoints = []
F_ypoints = []
f_mark_ypoints = []
y_akse_info = []

n=0
for n in range(x_akse_info[2]):
    f_ypoints.append(f(x_akse[n]))
    F_ypoints.append(F(x_akse[n]))
    f_mark_ypoints.append(f_mark(x_akse[n]))

info_listen.extend(f_ypoints)
info_listen.extend(F_ypoints)
info_listen.extend(f_mark_ypoints)
y_akse_info.append(min(info_listen))
y_akse_info.append(max(info_listen))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

k = [0, 0]

f_graf, = plt.plot(f_xpoints, f_ypoints, label="f(x) = "+ f_str.replace("**", "^"))
F_graf, = plt.plot(F_xpoints, F_ypoints, label="F(x) = " + F_str.replace("**", "^"))
f_mark_graf, = plt.plot(f_mark_xpoints, f_mark_ypoints, label="f'(x) = "+ f_mark_str.replace("**", "^"))

x_akse_graf, = plt.plot(x_akse_info[0:2], k, linestyle = 'dotted', color="black")
y_akse_graf, = plt.plot(k, y_akse_info[0:2], linestyle = 'dotted', color="black")

leg = plt.legend(loc='upper left')

plt.ion()
plt.show()

status = 1
while status != 0:
    x_value = float(input("x = "))

    print("f("+str(x_value)+") = " + str(f(x_value)))
    print("f'("+str(x_value)+") = " + str(f_mark(x_value)))
    print("F("+str(x_value)+") = " + str(F(x_value)))

    plt.plot(x_value, f(x_value), marker = 'o')
    plt.plot(x_value, F(x_value), marker = 'o')
    plt.plot(x_value, f_mark(x_value), marker = 'o')

    plt.annotate(text=str(f(x_value)), xy=(x_value, f(x_value)))
    plt.annotate(text=str(F(x_value)), xy=(x_value, F(x_value)))
    plt.annotate(text=str(f_mark(x_value)), xy=(x_value, f_mark(x_value)))
