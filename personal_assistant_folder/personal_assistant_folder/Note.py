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

    def add_edit(self, field_name, value):
        try:
            if hasattr(self, field_name):
                setattr(self, field_name, value)
        except ValueError:
            raise ValueError('invalid data to edit')

    def remove(self, field_name):
        if field_name == 'title':
            raise ValueError('You can`t delete note`s title')
        try:
            if hasattr(self, field_name):
                setattr(self, field_name, None)
        except ValueError:
            raise ValueError('invalid field name to remove')

    def __str__(self):
        tags_str = ', '.join(str(tag) for tag in self.tags) if self.tags else ''
        return f'Title: {self.title}\nContent: {self.content}\nTags: {tags_str}'