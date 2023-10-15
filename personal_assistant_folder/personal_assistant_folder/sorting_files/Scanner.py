from pathlib import Path


class Scanner:
    IMAGES = ('JPEG', 'PNG', 'JPG', 'SVG')
    VIDEOS = ('AVI', 'MP4', 'MOV', 'MKV')
    DOCUMENTS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    AUDIOS = ('MP3', 'OGG', 'WAV', 'AMR')
    ARCHIVES = ('ZIP', 'GZ', 'TAR')

    def __init__(self):
        self.images_files = list()
        self.videos_files = list()
        self.docs_files = list()
        self.audios_files = list()
        self.archives_files = list()
        self.other_files = list()

        self.folders = list()

        self.extensions = set()
        self.unknown_extensions = set()

        self.registered_extensions = {
            'IMAGES': self.images_files,
            'VIDEOS': self.videos_files,
            'DOCUMENTS': self.docs_files,
            'AUDIOS': self.audios_files,
            'ARCHIVES': self.archives_files
        }

    def _get_extensions(self, file_name):
        """
        Get file extension

        :param file_name: File name
        :return: file extension in uppercase
        """
        return Path(file_name).suffix[1:].upper()

    def scan(self, folder):
        """
        Scan and save in lists oll files and folders in folder

        :param folder: Path to folder which need sort
        """
        for item in folder.iterdir():
            if item.is_dir():
                if item.name not in ('IMAGES', 'VIDEOS', 'DOCUMENTS', 'AUDIOS', 'ARCHIVES'):
                    self.folders.append(item)
                    self.scan(item)
                continue

            extension = self._get_extensions(file_name=item.name)

            file_path = folder / item.name

            if not extension:
                self.other_files.append(file_path)
            else:
                try:
                    container = self.registered_extensions[extension]
                    self.extensions.add(extension)
                    container.append(file_path)
                except KeyError:
                    self.unknown_extensions.add(extension)
                    self.other_files.append(file_path)
