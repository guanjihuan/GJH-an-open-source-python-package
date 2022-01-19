import guan
import numpy as np

# calculate conductance
fermi_energy_array = np.linspace(-5, 5, 400)
h00 = guan.finite_size_along_one_direction(4)
h01 = np.identity(4)
conductance_array = guan.calculate_conductance_with_fermi_energy_array(fermi_energy_array, h00, h01)
guan.plot(fermi_energy_array, conductance_array, xlabel='E', ylabel='Conductance', type='-o')

# calculate scattering matrix
fermi_energy = 0
h00 = guan.finite_size_along_one_direction(4)
h01 = np.identity(4)
guan.print_or_write_scattering_matrix(fermi_energy, h00, h01)