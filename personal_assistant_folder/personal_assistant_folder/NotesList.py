from Note import Note


class NotesList:
    def __init__(self, file_name=None):
        self.noteslist = list()

    def _unique_title(self, value):
        for note in self.noteslist:
            if str(note.title) == value:
                raise ValueError('This Title already exist!')

    def add(self, value):
        # !!!Attention!!!
        # value - string from 3 part separate ';'
        # tags in value separate ','
        # Example: Title;Content;#tag1,#tag2,#tag3

        try:
            title, content, tags = value.split(';')
            self._unique_title(title)  # Перевірка на унікальність title
            note = Note(title, content)

            if tags:
                tags_list = tags.split(',')
                for tag in tags_list:
                    note.add_tag(tag)

            self.noteslist.append(note)

        except ValueError:
            raise ValueError("Invalid data format\nExample: Title;Content;#tag1,#tag2,#tag3")

    def edit_note(self, note_title, data, field=None):
        note_to_edit = None
        for note in self.noteslist:
            if note.title.value == note_title:
                note_to_edit = note

        if not note_to_edit:
            raise ValueError(f"Note with title '{note_title}' not found")

        try:
            if field is None:  # редагування всих полів
                title, content, tags = data.split(';')
                note_to_edit.title.value, note_to_edit.content.value = title, content
                note_to_edit.tags.clear()
                if tags:
                    tags_list = tags.split(',')
                    for tag in tags_list:
                        note_to_edit.add_tag(tag)
            # редагування відповідних полів
            elif field == 'title':
                note_to_edit.title.value = data
            elif field == 'content':
                note_to_edit.content.value = data
            elif field == 'tags':
                note_to_edit.tags.clear()
                tags_list = data.split(',')
                for tag in tags_list:
                    note_to_edit.add_tag(tag)
            else:
                raise ValueError("Invalid field name for editing")
        except ValueError:
            raise ValueError("Invalid data for editing\nExample: title;content;#tag1,#tag2,#tag3, or single one")

    def delete(self, value):
        # !!!Attention!!!
        # Find and delete Note work only by it title
        try:
            for note in self.noteslist:
                if str(note.title) == value:
                    self.noteslist.remove(note)
        except ValueError:
            pass

    def find_note(self, value):
        for note in self.noteslist:
            if str(note.title) == value:
                return note

    def find_notes(self, value):
        found_notes = []
        for note in self.noteslist:
            if value in note.title.value or value in note.content.value:
                found_notes.append(note)

        if not found_notes:
            found_notes.append('Nothing found!')

        return found_notes

    def find_sort(self, value: str):
        result_list = []
        title_to_note = {}

        for note in self.noteslist:
            for tag in note.tags:
                if value == tag.value:
                    title = note.title.value
                    if title not in title_to_note:
                        title_to_note[title] = note

        found_titles = list(title_to_note.keys())
        found_titles.sort()

        for title in found_titles:
            result_list.append(title_to_note[title])

        return result_list
