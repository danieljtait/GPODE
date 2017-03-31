import numpy as np
import matplotlib.pyplot as plt
from gp_src import ksqexp, GaussianProcess
from scipy.integrate import odeint

theta = 1.3
def dXdt(X, t, gp):
    return -theta*X + gp.interp_evalf(t)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

tp = np.linspace(0., 3.5, 51)
m = np.zeros(tp.size)
nsim = 5

for i in range(nsim):

    gp = GaussianProcess(ksqexp, kernel_par=5.)
    # Simulate

    rf = gp.sim(tp)
    gp.interp_fit(tp, rf)

    sol = odeint(dXdt, 1., tp, args=(gp,))

    ax1.plot(tp, rf, 'k-', alpha=0.2)
    ax2.plot(tp, sol, 'k-', alpha=0.2)

    m += sol[:,0]

#ax.plot(tp, m/nsim)

plt.show()