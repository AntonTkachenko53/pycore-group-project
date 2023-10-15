from notes.Title import Title
from notes.Content import Content


class Note:
    def __init__(self, title, content=''):
        self.title = Title(title)
        self.content = Content(content)
