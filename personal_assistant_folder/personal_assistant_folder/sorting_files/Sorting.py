import shutil
import sys
from personal_assistant_folder.sorting_files.Scanner import Scanner
from personal_assistant_folder.sorting_files.NormalizeName import NormalizeName
from pathlib import Path


class Sorting:
    def _prepare_folder_path(self, value):
        """
        # Get full path for sorting folder

        :param value: user path
        :return: full path
        """
        return Path(value).resolve()

    def __init__(self, folder_path):
        self.folder_path = self._prepare_folder_path(folder_path)
        self.scanner = Scanner()
        self.normalize_name = NormalizeName()

    def handle_file(self, path, root_folder, new_folder):
        """
        # Move file to new folder

        :param path: Main folder for sort
        :param root_folder: path to file
        :param new_folder: new path to file
        """
        target_folder = root_folder / new_folder
        target_folder.mkdir(exist_ok=True)
        path.replace(target_folder / self.normalize_name.new_name(path.name))

    def handle_archive(self, path, root_folder, new_folder):
        """
        Unpack archive in archives folder

        :param path: Main folder for sort
        :param root_folder: path to file
        :param new_folder: new path to folder with archive files
        :return:
        """
        target_folder = root_folder / new_folder
        target_folder.mkdir(exist_ok=True)

        new_name = self.normalize_name.new_name(path.name[:path.name.rfind('.')])

        archive_folder = target_folder / new_name
        archive_folder.mkdir(exist_ok=True)

        try:
            shutil.unpack_archive(str(path.resolve()), str(archive_folder.resolve()))
        except shutil.ReadError:
            archive_folder.rmdir()
            return

        path.unlink()

    def remove_empty_folders(self, path):
        """
        Delete empty folder

        :param path: path to folder
        """
        for item in path.iterdir():
            if item.is_dir():
                self.remove_empty_folders(item)
                try:
                    item.rmdir()
                except OSError:
                    pass

    def get_folder_objects(self, root_path):
        """
        Find and remove empty folders

        :param root_path: Main folder for sort
        """
        for folder in root_path.iterdir():
            if folder.is_dir():
                self.remove_empty_folders(folder)
                try:
                    folder.rmdir()
                except OSError:
                    pass

    def sort(self):
        """
        Start function script
        """

        self.scanner.scan(self.folder_path)

        for file in self.scanner.images_files:
            self.handle_file(file, self.folder_path, 'IMAGES')

        for file in self.scanner.videos_files:
            self.handle_file(file, self.folder_path, 'VIDEOS')

        for file in self.scanner.docs_files:
            self.handle_file(file, self.folder_path, 'DOCUMENTS')

        for file in self.scanner.audios_files:
            self.handle_file(file, self.folder_path, 'AUDIOS')

        for file in self.scanner.other_files:
            self.handle_file(file, self.folder_path, 'OTHERS')

        for file in self.scanner.archives_files:
            self.handle_archive(file, self.folder_path, 'ARCHIVES')

        self.get_folder_objects(self.folder_path)


if __name__ == '__main__':
    sorting = Sorting(sys.argv[1])
    sorting.sort()
