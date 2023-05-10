from os import path, getcwd


class Book:
    @classmethod
    def parse_file(cls, file_path=path.join(getcwd(), 'static', 'Alice-Book.txt')):
        if path.exists(file_path):
            book = cls()

            with open(file_path, 'r') as reader:
                for line in reader:
                    book.add_line(Line.create_line(line.strip()))

            print(f"Book has {book.total_lines(include_empty_lines=True)} lines. Valid lines count: {book.valid_lines_count} Emtpy lines count: {book.empty_lines_count}")
        else:
            print(f"File '{file_path}' does not exists.")

    def __init__(self):
        self.empty_lines_count = 0
        self.valid_lines_count = 0
        self.lines = list()

    def add_line(self, line):
        if not line.is_blank_line():
            self.valid_lines_count += 1
            self.lines.append(line)
        else:
            self.empty_lines_count += 1

    def total_lines(self, include_empty_lines=False):
        total = self.valid_lines_count

        if include_empty_lines:
            total += self.empty_lines_count

        return total


class Line:
    @classmethod
    def create_line(cls, content):
        parsed_content = content.strip()

        line = cls(len(parsed_content))

        if not line.is_blank_line():
            possible_words = filter(Word.is_valid_word, parsed_content.split())
            line.add_words(possible_words)

        return line

    def __init__(self, length):
        self.length = length
        self.words = set()

    def is_blank_line(self):
        return self.length == 0

    def add_words(self, another_words):
        self.words.union(another_words)


class Word:
    def __init__(self, content):
        self.content = content

    @classmethod
    def is_valid_word(cls, content):
        return isinstance(content, str) and len(content) > 0


Book.parse_file()
