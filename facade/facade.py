#It holds the software interface
from controllers import store_files, optimizer


def upload_files(file_path, file_name):
    store_files.upload_files(file_path, file_name)


def optimize():
    return optimizer.controller_optimize()


def configure_pso():
    pass


def download_results():
    pass


def configure_simulation():
    pass


def cell_details():
    pass
