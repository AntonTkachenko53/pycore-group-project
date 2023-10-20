from personal_assistant_folder.notes.Title import Title
from personal_assistant_folder.notes.Content import Content
from personal_assistant_folder.notes.Tag import Tag


class Note:
    def __init__(self, title, content=''):
        self.title = Title(title)
        self.content = Content(content)
        self.tags = set()

    def edit_title(self, value):
        self.title = Title(value)

    def edit_content(self, value):
        self.content = Content(value)

    def add_tag(self, value):
        """
        Add new tag in tags list for note
        :param value: new tag
        """
        value = value.strip()

        if not self.check_tag(value):
            self.tags.add(Tag(value))

    def check_tag(self, value):
        """
        Check in note has this tag
        :param value: it`s tag which need check
        :return: True if it has. False if not
        """
        value = value.strip()

        return True if Tag(value) in self.tags else False

    def delete_tag(self, value):
        """
        Delete tag from tags list for note
        :param value: tag
        """
        value = value.strip()

        if self.check_tag(value):
            self.tags.discard(Tag(value))

    def __str__(self):
        tags_str = ', '.join(str(tag) for tag in self.tags) if self.tags else ''
        return (f"{'Title:'.ljust(8)} {self.title}\n"
                f"{'Content:'.ljust(8)} {self.content}\n"
                f"{'Tags:'.ljust(8)} {tags_str}")
