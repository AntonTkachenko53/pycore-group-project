from notes.Title import Title
from notes.Content import Content
from notes.Tag import Tag


class Note:
    def __init__(self, title, content=''):
        self.title = Title(title)
        self.content = Content(content)
        self.tags = set()

    def add_tag(self, value):
        """
        Add new tag in tags list for note
        :param value: new tag
        """
        if not self.check_tag(value):
            self.tags.add(Tag(value))

    def check_tag(self, value):
        """
        Check in note has this tag
        :param value: it`s tag which need check
        :return: True if it has. False if not
        """
        return True if Tag(value) in self.tags else False

    def delete_tag(self, value):
        """
        Delete tag from tags list for note
        :param value: tag
        """
        if self.check_tag(value):
            self.tags.discard(Tag(value))
