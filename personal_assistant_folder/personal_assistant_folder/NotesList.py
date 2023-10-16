from Note import Note


class NotesList:
    def __init__(self):
        self.noteslist = list()

    # def _unique_title(self, value):
    #     for note in self.noteslist:
    #         if str(note.title) == value:
    #             raise ValueError('This Title already exist!')

    def add(self, value):
        # !!!Attention!!!
        # value - string from 3 part separate ';'
        # tags in value separate ','
        # Example: Title;Content;#tag1,#tag2,#tag3

        try:
            title, content, tags = value.split(';')

            note = Note(title, content)

            if tags:
                tags_list = tags.split(',')
                for tag in tags_list:
                    note.add_tag(tag)

            self.noteslist.append(note)

        except ValueError:
            raise ValueError("Invalid data format\nExample: Title;Content;#tag1,#tag2,#tag3")

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
        found_notes = []
        for note in self.noteslist:
            if value in note.title or value in note.content:
                found_notes.append(note)
        return found_notes        