"""LINKED LIST
"""


class Song():
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.previous = None

    def show_song(self):
        print("----------------------------")
        print("| {} | {} | {} |".format(self.title, self.artist, self.duration))
        print("----------------------------")


def main():
    song1 = Song("1. 1 on 1", "Jass_Dhillon", 3.45)
    song2 = Song("2. Jail", "Sidhu_Moosewala", 4.23)
    song3 = Song("3. Getto", "Akon", 3.65)
    song4 = Song("4. Kalla_Chann", "Sharry_Maan", 4.53)
    song5 = Song("5. Bad_Guy", "Billie_Eilish", 3.12)

    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song5
    song5.next = song1

    song1.previous = song5
    song2.previous = song1
    song3.previous = song2
    song4.previous = song3
    song5.previous = song4

    temp = song1

    while temp.next != song1:
        temp.show_song()
        temp = temp.next

    temp.show_song()

    temp = song5
    while temp.previous != song5:
        temp.show_song()
        temp = temp.previous

    temp.show_song()

if __name__ == '__main__':
    main()
