from file_handler import prn_reader
from reflectance import reflectance
import cmath


class Error_Function:

    # It should receive a list with the angle and the correspondent reflectance.
    def __init__(self, data):
        self.file_path = ""
        self.wavelength = ""
        self.permittivity_real_2 = ""
        self.permittivity_imag_2 = ""
        self.permittivity_glass = ""
        self.experimental_data = data

    def get_error(self, wavelength, permittivity_real_2, permittivity_imag_2, permittivity_real_3,
                  permittivity_imag_3, permittivity_glass, thickness):
        experimental_data = prn_reader.get_normalized_experimental_table(self.file_path)
        error = 0

        for i in range(len(experimental_data)):
            angle_radians = experimental_data[i][0] * cmath.pi / 180

            reflectance_experimental = experimental_data[i][1]
            reflectance_calculated = reflectance.total_reflectance(angle_radians, wavelength, permittivity_real_2,
                                                                   permittivity_imag_2, permittivity_real_3,
                                                                   permittivity_imag_3, permittivity_glass, thickness)
            error = error + (reflectance_experimental - reflectance_calculated) ** 2
        return error

    def get_error(self, params):
        experimental_data = self.experimental_data
        error = 0

        for i in range(len(experimental_data)):
            angle_radians = experimental_data[i][0] * cmath.pi / 180

            reflectance_experimental = experimental_data[i][1]

            reflectance_calculated = reflectance.total_reflectance(
                angle_radians,
                self.wavelength,
                self.permittivity_real_2,
                self.permittivity_imag_2,
                params[0],
                params[1],
                self.permittivity_glass,
                params[2])

            error = error + (reflectance_experimental - reflectance_calculated) ** 2

        return error
