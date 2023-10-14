from pathlib import Path


class Scanner:
    def __init__(self):
        self.IMAGES = ('JPEG', 'PNG', 'JPG', 'SVG')
        self.VIDEOS = ('AVI', 'MP4', 'MOV', 'MKV')
        self.DOCUMENTS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
        self.AUDIOS = ('MP3', 'OGG', 'WAV', 'AMR')
        self.ARCHIVES = ('ZIP', 'GZ', 'TAR')

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
                    if extension in self.IMAGES:
                        container = self.registered_extensions['IMAGES']
                        extensions_list = self.extensions
                    elif extension in self.VIDEOS:
                        container = self.registered_extensions['VIDEOS']
                        extensions_list = self.extensions
                    elif extension in self.DOCUMENTS:
                        container = self.registered_extensions['DOCUMENTS']
                        extensions_list = self.extensions
                    elif extension in self.AUDIOS:
                        container = self.registered_extensions['AUDIOS']
                        extensions_list = self.extensions
                    elif extension in self.ARCHIVES:
                        container = self.registered_extensions['ARCHIVES']
                        extensions_list = self.extensions
                    else:
                        container = self.other_files
                        extensions_list = self.unknown_extensions

                    extensions_list.add(extension)
                    container.append(file_path)

                except KeyError:
                    self.unknown_extensions.add(extension)
                    self.other_files.append(file_path)
