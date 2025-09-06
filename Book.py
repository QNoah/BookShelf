class Book:
    def __init__(self, title="", category="", author="", total_pages=0, read_pages=0):
        self.title = title
        self.category = category
        self.author = author
        self.total_pages = total_pages
        self.read_pages = read_pages
        self.read = False

    def add_read(self, read: int):
        if self.read_pages + read >= self.total_pages:
            self.read_pages = self.total_pages
            self.read = True
            return
        self.read_pages + read

    def finish_Reading(self):
        self.read_pages = self.total_pages
