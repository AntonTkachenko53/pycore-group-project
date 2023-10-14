import shutil
import sys
from pathlib import Path
from sort_files.Scanner import Scanner
from sort_files.NormalizeName import NormalizeName


class Sorting:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path).resolve()
        self.scanner = Scanner()
        self.normalize_name = NormalizeName()

    def _prepare_folder_path(self, value):
        return Path(value).resolve()

    def _create_folder(self, path):
        path.mkdir(parents=True, exist_ok=True)

    def _remove_empty_folders(self, path):
        for item in path.iterdir():
            if item.is_dir():
                self._remove_empty_folders(item)
                try:
                    item.rmdir()
                except OSError:
                    pass

    def _rename_file(self, file, category):
        target_folder = self.folder_path / category
        self._create_folder(target_folder)
        new_name = self.normalize_name.new_name(file.name)
        file.rename(target_folder / new_name)

    def _handle_archive(self, archive, category):
        target_folder = self.folder_path / category
        self._create_folder(target_folder)
        new_name = self.normalize_name.new_name(archive.stem)
        archive_folder = target_folder / new_name
        self._create_folder(archive_folder)

        try:
            shutil.unpack_archive(archive, archive_folder)
            archive.unlink()
        except shutil.ReadError:
            archive_folder.rmdir()

    def sort(self):
        self.scanner.scan(self.folder_path)

        for category, files in self.scanner.categories.items():
            if category != "ARCHIVES":
                for file in files:
                    self._rename_file(file, category)
            else:
                for archive in files:
                    self._handle_archive(archive, category)

        self._remove_empty_folders(self.folder_path)


if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python sorting_script.py <folder_path>")
    else:
        sorting = Sorting(sys.argv[1])
        sorting.sort()
