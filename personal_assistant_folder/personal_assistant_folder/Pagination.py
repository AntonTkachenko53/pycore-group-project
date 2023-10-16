class Paginator:
    def __init__(self, data, num_of_records=5):
        self.data = list(data.values())
        self.num_of_records = num_of_records

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = []
            last_index = self.index + self.num_of_records
            for index in range(self.index, last_index):
                if index < len(self.data):
                    result.append(self.data[index])
                else:
                    break
            self.index += self.num_of_records
            return result
        else:
            raise StopIteration
