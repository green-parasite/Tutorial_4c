import numpy as np
import matplotlib.pyplot as plt

number_of_points = 100
extreme_position = 10.
y_label = r'$U(r)$'
x_label = r'$r$'
axislabel_fontsize = 16
tickmark_fontsize = 14
whitespace_factor = 0.02

plt.rcParams.update({
    "text.usetex": False,
    "font.family": "serif"})

positions = np.linspace(1./number_of_points, extreme_position,
                        num=number_of_points)


# def harmonic(position, coefficient, equilibrium=0.):
#     return 0.5 * coefficient * (position-equilibrium)**2


# def linear(position, coefficient, zero_point=0.):
#     return coefficient * (position-zero_point)


def reciprocal(position, coefficient, origin=0.):
    return coefficient / (position - origin)


# def lj(position, binding_energy, equilibrium_position, n=6):
#     scaled_position = equilibrium_position / position
#     return binding_energy/scaled_position



G = 6.67e-11
m = 2
M = 20*m
binding_energy = G*M*m
r_naught = 2.
linear_coefficient = 4.
lj_power = r_naught * np.sqrt(linear_coefficient / (2 * binding_energy))


k = -3
x = np.linspace(0.01, .127, 100)
#argument = k+(1/x)
#print(argument)
k = np.abs(k)

time = (x/k)*np.sqrt(k+(1/x))/k - np.arctanh(np.sqrt(k+(1/x))/np.power(k, 3/2))
print(time)
#exit()

figures, axs = plt.subplots(1, 2)
y = -3
axs[1].plot(x, time)


# Lennard-Jones potential
# potential = lj(positions, binding_energy, r_naught, n=lj_power)
# axes.set_xlim(0., extreme_position)
# axes.set_ylim(-1.5*binding_energy, 1.5*binding_energy)
# axes.xaxis.set_label_coords(1.+whitespace_factor, 0.5)

# Reciprocal potential
potential = reciprocal(positions, -linear_coefficient)
axs[0].set_xlim(0., extreme_position)
axs[0].set_ylim(-4*linear_coefficient, (1.+whitespace_factor)*linear_coefficient)
axs[0].xaxis.set_label_coords(1.+whitespace_factor, 0.80)
axs[0].axhline(y=y, xmin=0, xmax=.127)
axs[0].plot(positions, potential)
axs[0].set_xlabel(x_label, verticalalignment='center', horizontalalignment='left', fontsize=axislabel_fontsize)
axs[0].set_ylabel(y_label, rotation='horizontal', fontsize=axislabel_fontsize)
axs[0].yaxis.set_label_coords(0., 1.+whitespace_factor)

axs[0].plot(0, 1, ls="", marker="^", ms=5, color="k",
          transform=axs[0].get_xaxis_transform(), clip_on=False)
axs[0].plot(1, 0, ls="", marker=">", ms=5, color="k",
          transform=axs[0].get_yaxis_transform(), clip_on=False)

# axs[0].set_xticks([])
# axs[0].set_yticks([0.])
# axs[0].tick_params(axis='y', labelsize=tickmark_fontsize)

# axs[0].spines["right"].set_visible(False)
# axs[0].spines["left"].set_position(("data", 0.))
# axs[0].spines["top"].set_visible(False)
# axs[0].spines["bottom"].set_position(("data", 0.))

plt.show()
print(time)

