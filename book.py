import itertools

class Book:
    id_iter = itertools.count()
    def __init__(self, id:int = next(id_iter), title: str = None, category: str = None, author:str = None, total_pages: int = 0, read_pages: int = 0):
        self.id = id
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
