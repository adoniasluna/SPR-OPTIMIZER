from reflectance import glass_permittivity as gp
from pso.pso import PSO
from fitness.squared_error import Error_Function
from file_handler import prn_reader
import os


def Exec1(path):
    data = prn_reader.get_normalized_experimental_table(path)
    Error = Error_Function(data)
    Error.wavelength = 975.1
    Error.permittivity_real_2 = 1
    Error.permittivity_imag_2 = 0
    Error.permittivity_glass = gp.BK7(975.1)

    return Error


def controller_optimize():
    # Get the list with all the prn files
    dir_path = "/home/adonias/PycharmProjects/mysite/media"
    prn_files = os.listdir(dir_path)

    # Defining the parameters o the simulation
    dimensions = [(-60.261, -21), (-9.4685, 1.95), (500, 2500)]
    num_particles = 50
    max_iterations = 10

    best_positions = []
    # Loop through all the files on the directory and run the PSO
    for file_name in prn_files:
        file_path = dir_path + "/" + file_name
        p = PSO(Exec1(file_path).get_error, dimensions, num_particles, max_iterations)
        best_positions.append(p.best_position)

    return best_positions