import cmath
import math


def k_metal(angle, wavelength, permittivity_real, permittivity_imag, glass_permittivity):
    return k_aux(angle, wavelength, permittivity_real, permittivity_imag, glass_permittivity)


def k_air(angle, wavelength, permittivity_real, permittivity_imag, glass_permittivity):
    return k_aux(angle, wavelength, permittivity_real, permittivity_imag, glass_permittivity)


def k_glass(angle, wavelength, glass_permittivity):
    return k_aux(angle, wavelength, glass_permittivity, 0, glass_permittivity)


def k_aux(angle, wavelength, permittivity_real, permittivity_imag, glass_permittivity):
    sqrt_part = cmath.sqrt(
        permittivity_real + 1j * permittivity_imag - glass_permittivity * (cmath.sin(angle) ** 2))
    wave_number = (2 * math.pi) / wavelength * sqrt_part
    return wave_number.real - abs(wave_number.imag) * 1j
