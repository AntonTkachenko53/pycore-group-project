class Paginator:
    def __init__(self, data: list, num_of_records=5):
        self.data = data
        self.num_of_records = num_of_records
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        start_index = self.current_page * self.num_of_records
        last_index = start_index + self.num_of_records
        page_data = self.data[start_index:last_index]

        if not page_data:
            raise StopIteration
        return page_data

    def move(self, direction):
        if direction == 'n' and (self.current_page + 1) * self.num_of_records < len(self.data):
            self.current_page += 1
        elif direction == 'p' and self.current_page > 0:
            self.current_page -= 1
        elif direction == 'q':
            raise StopIteration
