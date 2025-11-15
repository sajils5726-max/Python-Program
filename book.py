class Publisher:
    def __init__(self, name):
        self.name = name


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def show(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Pages:", self.pages)


p = Python("ABC Publishers", "Learn Python", "Guido", 450, 350)
p.show()
