class ArtGallery:
    def __init__(self, name):
        self.name = name
        self.artworks = []
        print("Gallery", self.name, "opened")

    def add_artwork(self):
        title = input("Title: ")
        artist = input("Artist: ")
        self.artworks.append([title, artist])
        print("Added")

    def show_artworks(self):
        if len(self.artworks) == 0:
            print("No artworks")
        else:
            print("Artworks:")
            for art in self.artworks:
                print(art[0], "by", art[1])

    def __del__(self):
        print("Gallery", self.name, "closed")

name = input("Gallery name: ")
g = ArtGallery(name)

while True:
    print("1. Add 2. Show 3. Exit")
    c = input("Choice: ")
    if c == "1":
        g.add_artwork()
    elif c == "2":
        g.show_artworks()
    elif c == "3":
        del g
        break