import os

class FileReader:
    """
        чтения файлов
    """
    @staticmethod
    def read_file(file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} not found")
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Permission denied to read file {file_path}")

        with open(file_path, 'r') as file:
            return file.readlines()