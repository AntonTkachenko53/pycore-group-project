import pickle
import os


class Serialization:
    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        return None
