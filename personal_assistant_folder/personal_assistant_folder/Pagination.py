import math


class Paginator:
    def __init__(self, data: list, num_of_records=5):
        self.data = data
        self.total_pages = math.ceil(len(data) / num_of_records)
        self.num_of_records = num_of_records
        self.current_page = 1

    def __iter__(self):
        return self

    def __next__(self):
        start_index = (self.current_page - 1) * self.num_of_records
        last_index = start_index + self.num_of_records
        page_data = self.data[start_index:last_index]

        if not page_data:
            raise StopIteration
        return page_data

    def move(self, direction):
        if direction == 'n' and self.current_page < self.total_pages:
            self.current_page += 1
        elif direction == 'p' and self.current_page > 1:
            self.current_page -= 1
        elif direction == 'q':
            raise StopIteration