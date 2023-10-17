import pickle
import os
from shutil import copy


class Serialization:
    @staticmethod
    def save_to_file(data, filename):
        backup_file = filename + '.backup'
        if os.path.exists(filename):
            copy(filename, backup_file)
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
        except Exception:
            if os.path.exists(backup_file):
                copy(backup_file, filename)
            raise

    @staticmethod
    def load_from_file(filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'rb') as file:
                    return pickle.load(file)
            except Exception:
                raise
        return None
