class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def open(self):
        print(f"Opening {self.name}")


class GoogleDoc(File):
    def edit(self):
        print(f"Editing Google Doc: {self.name}")


class GoogleSheet(File):
    def calculate(self):
        print(f"Calculating in Google Sheet: {self.name}")


class GoogleSlide(File):
    def present(self):
        print(f"Presenting Google Slide: {self.name}")


doc = GoogleDoc("Resume", 120)

doc.open()
doc.edit()