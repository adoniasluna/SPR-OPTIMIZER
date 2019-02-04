from reflectance import wavenumber
import cmath

def total_reflectance(angle, wavelength, permittivity_real_2, permittivity_imag_2, permittivity_real_3,
                      permittivity_imag_3,
                      permittivity_glass, thickness):

    k2 = wavenumber.k_air(angle, wavelength, permittivity_real_2, permittivity_imag_2, permittivity_glass)

    reflectance12 = reflectance_interface_12(angle, wavelength, permittivity_real_2, permittivity_imag_2,
                                             permittivity_glass, k2)
    reflectance23 = reflectance_interface_23(angle, wavelength, permittivity_real_2, permittivity_imag_2,
                                             permittivity_real_3, permittivity_imag_3, permittivity_glass, k2)

    numarator = reflectance12 + reflectance23 * cmath.exp(-2j * thickness * k2)
    denominator = 1 + (reflectance12 * reflectance23 * cmath.exp(-2j * thickness * k2))

    return abs(numarator / denominator) ** 2


def reflectance_interface_12(angle, wavelength, permittivity_real_2, permittivity_imag_2, permittivity_glass, k2):
    k1 = wavenumber.k_glass(angle, wavelength, permittivity_glass)

    numarator = (permittivity_real_2 + 1j * permittivity_imag_2) * k1 - permittivity_glass * k2
    denominator = (permittivity_real_2 + 1j * permittivity_imag_2) * k1 + permittivity_glass * k2

    return numarator / denominator


def reflectance_interface_23(angle, wavelength, permittivity_real_2, permittivity_imag_2, permittivity_real_3,
                             permittivity_imag_3,
                             permittivity_glass, k2):

    k3 = wavenumber.k_metal(angle, wavelength, permittivity_real_3, permittivity_imag_3, permittivity_glass)

    numarator = (permittivity_real_3 + 1j * permittivity_imag_3) * k2 - (
                                                                        permittivity_real_2 + 1j * permittivity_imag_2) * k3
    denominator = (permittivity_real_3 + 1j * permittivity_imag_3) * k2 + (
                                                                          permittivity_real_2 + 1j * permittivity_imag_2) * k3

    return numarator / denominator
