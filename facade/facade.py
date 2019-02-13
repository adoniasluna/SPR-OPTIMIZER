# It holds the software interface
from controllers import store_files, optimizer


def upload_files(file_path, file_name):
    store_files.upload_files(file_path, file_name)


def optimize(files, num_particles, max_iterations, inertia_weight, cognitive_constant, social_constant):
    return optimizer.controller_optimize(files, num_particles, max_iterations, inertia_weight, cognitive_constant,
                                         social_constant)


def configure_pso():
    pass


def download_results():
    pass


def configure_simulation():
    pass


def cell_details():
    pass
