import pickle
import os


class Serialization:
    @staticmethod
    def save_to_file(data, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
        except Exception:
            raise

    @staticmethod
    def load_from_file(filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'rb') as file:
                    return pickle.load(file)
            except Exception:
                raise
        return []
