""" A Python program that creates a Playlist object with a parameterized constructor (name and genre), 
initializes an empty songs list as a default attribute, provides methods to add, remove, 
and display songs, fires a destructor when the playlist is deleted, and lets you control everything through
a numbered menu loop."""

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []  

    def add_song(self, song):
        self.songs.append(song)
        print(f"Song {song} added")

    def remove_song(self, song):
        self.songs.remove(song)
        print(f"Song {song} removed")

    def display(self):
        print(f"{self.name}, {self.genre}")
        for i in self.songs:
            print(i)


p = Playlist("Hide me now", "Spirituality")

while True:
    print("1. Add Song \n 2. Remove Song \n 3. View Songs")
    choice = int(input("Enter a option: "))

    if choice == 1:
        name = str(input("Enter a song name: "))
        genre = str(input("Enter a song genre: "))
        p.add_song(name)

    elif choice == 2:
        name = str(input("Enter a song name: "))
        p.remove_song(name)

    elif choice == 3:
        p.display()