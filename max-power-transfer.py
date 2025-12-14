import numpy as np
import matplotlib.pyplot as plt

# Elektrik devresi parametreleri
Vs = 5      # Volt
Rs = 100    # Ohm
T = 1        # RL artış miktarı
RL_min, RL_max = 20, 180

RL = np.arange(RL_min, RL_max + T, T)
PL = (Vs**2) * RL / ((Rs + RL)**2)

RL_deney = np.array([22, 47, 100, 150, 180])
PL_deney = (Vs**2) * RL_deney / ((Rs + RL_deney)**2)

# Grafik
plt.plot(RL, PL, label=r"$P_L$")
plt.scatter(RL_deney, PL_deney, label="Deney", color="red")
plt.xlabel(r"$R_L$ [$\Omega$]", fontsize=15)
plt.ylabel(r"$P_L$ [Watt]", fontsize=15)
plt.title("Yük Direncine Bağlı Güç Transferi", fontsize=15)
plt.legend(fontsize=15)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig("maksimum_guc_transferi.png", dpi=400)
plt.show()