from pathlib import Path


class Scanner:
    def __init__(self):
        self.extensions = {
            "IMAGES": ("JPEG", "PNG", "JPG", "SVG"),
            "VIDEOS": ("AVI", "MP4", "MOV", "MKV"),
            "DOCUMENTS": ("DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"),
            "AUDIOS": ("MP3", "OGG", "WAV", "AMR"),
            "ARCHIVES": ("ZIP", "GZ", "TAR"),
        }
        self.categories = {category: [] for category in self.extensions}
        self.unknown_extensions = set()

    def _get_extension(self, file_name):
        return Path(file_name).suffix[1:].upper()

    def _categorize_file(self, file_path):
        extension = self._get_extension(file_path.name)

        for category, ext_list in self.extensions.items():
            if extension in ext_list:
                self.categories[category].append(file_path)
                return

        self.unknown_extensions.add(extension)
        self.categories["OTHER"].append(file_path)

    def _scan_folder(self, folder):
        for item in folder.iterdir():
            if item.is_dir() and item.name not in self.extensions:
                self._scan_folder(item)
            else:
                if item.is_file():
                    self._categorize_file(item)

    def scan(self, folder):
        folder_path = Path(folder)
        if not folder_path.is_dir():
            raise ValueError("The provided path is not a directory.")

        self._scan_folder(folder_path)
