def upload_files(file_path, f):
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
