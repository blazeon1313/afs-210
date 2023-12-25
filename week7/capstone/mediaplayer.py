import random

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
class Playlist:
    def __init__(self):
        self.playlist = []
        self.current = 0
        self.count = 0
    
    def addSong(self, song):
        self.playlist.append(song)
        self.count += 1
    
    def removeSong(self, song):
        if song in self.playlist:
            self.playlist.remove(song)

    def showPlaylist(self):
        for song in self.playlist:
            print(song)

    def showShuffledPlaylist(self):
        shuffled_playlist = list(self.playlist)  # Create a copy of the playlist
        random.shuffle(shuffled_playlist)  # Shuffle the copy
        print("\nShuffled Playlist Order:\n")
        for song in shuffled_playlist:
            print(song)

playlist = Playlist()

playlist.addSong(Song('Hero', 'Skillet'))
playlist.addSong(Song('Monster', 'Skillet'))
playlist.addSong(Song('I Can Only Imagine', 'Mercy Me'))
playlist.addSong(Song('Baby Blue', 'George Strait'))
playlist.addSong(Song('Angels Among Us', 'Alabama'))
playlist.addSong(Song('Paradise City', 'Guns ~N~ Roses'))

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        
        title = input("Enter song title: ")
        artist = input("Enter the artist name: ")
        
        # Add song to playlist
        newSong = Song(title, artist)
        playlist.addSong(newSong)
        print(47 * "-")
        print(f"{newSong} Added to Playlist")
    
    elif choice == 2:
        # Prompt user for Song Title
        title = input("Enter the song title to remove: ")
        artist = input("Enter the artist's name: ") 
        
        # remove song from playlist
        deleteSong = Song(title, artist)
        playlist.removeSong(deleteSong)
        print(47 * "-")
        print(f"{deleteSong} Removed to Playlist")
    
    elif choice == 3:
        # Play the playlist from the beginning        
        # Display song name that is currently playing
            print(47 * "-")
            print("Playing....")        
            print(playlist.playlist[0])
    
    elif choice == 4:
        # Skip to the next song on the playlist
        if len(playlist.playlist) > 0:
            playlist.current += 1
            playlist.current %= len(playlist.playlist)
        
        # Display song name that is now playing
            print("\nSkipping....\n")
            print(47 * "-") 
            print("Now Playing: ")
            print(playlist.playlist[playlist.current])
        else:
            print("Playlist is empty")
    
    elif choice == 5:
        # Go back to the previous song on the playlist
        if len(playlist.playlist) > 0:
            playlist.current -= 1
            playlist.current %= len(playlist.playlist)
        
        # Display song name that is now playing
            print(47 * "-")
            print("\nReplaying....\n") 
            print(playlist.playlist[playlist.current])
        else:
            print("Playlist is empty")  
    
    elif choice == 6:
        print(47 * "-")
        print("Shuffling....")
        
        # Randomly shuffle the playlist and play the first song
        playlist.showShuffledPlaylist()
        # Display song name that is now playing
        print("\nNow Playing: \n")
        print(playlist.playlist[playlist.current])          
    
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print(47 * "-")
        print("\nCurrently playing: \n", playlist.playlist[playlist.current])
    
    elif choice == 8:
        # Show the current song list order
        print(47 * "-")
        print("\nSong list:\n")
        playlist.showPlaylist()
    
    elif choice == 0:
        print("Goodbye.")
        break

            
