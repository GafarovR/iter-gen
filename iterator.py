class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_main = 0
        self.cursor_nested = -1
        return self

    def __next__(self):
        self.cursor_nested += 1
        if self.cursor_nested == len(self.list_of_list[self.cursor_main]):
            self.cursor_main += 1
            self.cursor_nested = 0
        if self.cursor_main == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.cursor_main][self.cursor_nested]
        return item


def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert (FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test()
