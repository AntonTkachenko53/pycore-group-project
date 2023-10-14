import re


class NormalizeName:
    def __init__(self, replace_space_with="_", transliteration_map=None):
        self.replace_space_with = replace_space_with
        self.transliteration_map = (
            transliteration_map
            if transliteration_map
            else self._build_transliteration_map()
        )

    def _build_transliteration_map(self):
        """
        Prepare Translation map
        :return: dictionary for translations
        """
        pass

    def new_name(self, text):
        """
        Generate transliterated and normalized name
        :param text: input text with Cyrillic characters
        :return: normalized and transliterated text
        """
        transliterated_text = text.translate(self.transliteration_map)
        normalized_text = re.sub(r"\W", self.replace_space_with, transliterated_text)

        return normalized_text


transliteration_map = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "д": "d",
    "е": "e",
    "є": "ie",
    "ж": "zh",
    "з": "z",
    "и": "y",
    "і": "i",
    "ї": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ь": "",
    "ю": "iu",
    "я": "ia",
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "H",
    "Д": "D",
    "Е": "E",
    "Є": "IE",
    "Ж": "ZH",
    "З": "Z",
    "И": "Y",
    "І": "I",
    "Ї": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TS",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ь": "",
    "Ю": "IU",
    "Я": "IA",
}

normalizer = NormalizeName(
    replace_space_with="_", transliteration_map=transliteration_map
)
normalized_text = normalizer.new_name("Hello World!")
print(normalized_text)
