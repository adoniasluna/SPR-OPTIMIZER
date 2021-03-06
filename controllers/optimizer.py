from reflectance import glass_permittivity as gp
from pso.pso import PSO
from fitness.squared_error import Error_Function
from file_handler import prn_reader
from os import listdir
from os.path import isfile, join


def exec1(path):
    data = prn_reader.get_normalized_experimental_table(path)
    error = Error_Function(data)
    error.wavelength = 975.1
    error.permittivity_real_2 = 1
    error.permittivity_imag_2 = 0
    error.permittivity_glass = gp.BK7(975.1)

    return error


def controller_optimize(files, num_particles, max_iterations, inertia_weight, cognitive_constant, social_constant,
                        initial_position):
    # Get the list with all the prn files
    dir_path = "media/"
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    # prn_files = listdir(dir_path)

    # Defining the parameters o the simulation
    dimensions = [(-60.261, -21), (-9.4685, 1.95), (500, 2500)]

    best_positions = []
    # Loop through all the files on the directory and run the PSO
    for fls in files:
        if fls in onlyfiles:
            file_path = dir_path + "/" + fls

            if initial_position == "RANDOM":
                p = PSO(exec1(file_path).get_error, dimensions, num_particles, max_iterations, inertia_weight,
                        cognitive_constant, social_constant)
                best_positions.append((p.best_position, p.best_error))
            else:
                # Function that calculates specific position to the particles
                pass

    return best_positions
