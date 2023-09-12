class Category:
    def __init__(self, category_filepath: str):
        self.filepath = category_filepath
        self.title = None
        self.words = []

        self.read_first_line_to_get_title()

    def read_first_line_to_get_title(self):
        open_generator = open(self.filepath)
        first_line = next(open_generator)
        open_generator.close()
        self.title = first_line.strip().split(":")[1]

    def get_words(self):
        with open(self.filepath) as fr:
            content_lines = fr.readlines()
        self.words = [word.rstrip() for word in content_lines[1:]]

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        return f"Category: {self.title}"
