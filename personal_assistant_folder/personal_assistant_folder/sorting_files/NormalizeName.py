import re


class NormalizeName:
    UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j",
                   "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts",
                   "ch", "sh", "sch", "", "ju", "ja")

    def _build_transliteration_map(self):
        """
        Prepare Translation map
        :return: dictionary for translations
        """
        trans = {}

        for key, value in zip(self.UKRAINIAN_SYMBOLS, self.TRANSLATION):
            trans[ord(key)] = value
            trans[ord(key.upper())] = value.upper()

        return trans

    def new_name(self, name):
        """
        Generate translation name
        :param name: file or folder name on cyrillic
        :return: new name on latin
        """
        new_name = name.translate(self._build_transliteration_map())
        new_name = re.sub(r'\W', "_", new_name)

        return new_name
