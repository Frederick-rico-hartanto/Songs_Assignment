class Song:
    def __init__(self, title, artist, year, status):
        self.title = title
        self.artist = artist
        self.year = year
        self.status = status


class SongsToLearnList:
    def __init__(self):
        self.songs = []

    def load_songs(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                data = line.strip().split(',')
                title, artist, year, status = data
                song = Song(title, artist, int(year), status)
                self.songs.append(song)

    def list_songs(self):
        learned_count = 0
        for i, song in enumerate(self.songs):
            status_icon = '*' if song.status == 'u' else ' '
            print(f"{i}. {status_icon} {song.title} - {song.artist} ({song.year})")

            if song.status == "l":
                learned_count += 1

        print(f"\n{learned_count} songs learned, {len(self.songs) - learned_count} songs still to learn")

    def add_song(self, title, artist, year, status):
        try:
            if not self.validate_year(year):
                return
            song = Song(title, artist, int(year), status)
            self.songs.append(song)
            print(f"{title} by {artist} added to the list.")
        except ValueError:
            print("Invalid input; enter a valid number")

    def validate_year(self, year):
        low = 0
        if int(year) < low:
            print("Number must be >= 0")
            return False
        else:
            return True

    def complete_song(self, index):
        try:
            if index < 0:
                print("Number must be more than or equal to 0")
            elif 0 <= index < len(self.songs):
                if self.songs[index].status == 'u':
                    self.songs[index].status = 'l'
                    print(f"{self.songs[index].title} marked as learned.")
                else:
                    print(f"{self.songs[index].title} is already marked as learned.")
            else:
                print("Invalid song number.")

        except ValueError:
            print("Invalid input; enter a valid number")

    def update_csv(self, file_path):
        with open(file_path, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.year},{song.status}\n")


class Run(SongsToLearnList):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Songs to Learn - by Frederick Rico Hartanto")
        file_path = "songs.csv"
        self.load_songs(file_path)
        print(f"({len(self.songs)}) Songs Loaded")

        MENU = """Menu:
        L - List songs
        A - Add new song
        C - Complete a song
        Q - Quit"""

        print(MENU)

        user_input = input(">>>").upper()

        while user_input != "Q":
            if user_input == "L":
                self.list_songs()
            elif user_input == "A":
                title = input("Title: ").strip()
                if not title:
                    print("Input can not be blank")
                    continue
                artist = input("Artist: ").strip()
                if not artist:
                    print("Input can not be blank")
                    continue
                year = input("Year: ").strip()
                if not self.validate_year(year):
                    continue
                status = input("Enter the status ('u' for unlearned, 'l' for learned): ").strip().lower()
                if status not in ['u', 'l']:
                    print("Invalid status. Please enter 'u' or 'l'.")
                    continue
                self.add_song(title, artist, year, status)
            elif user_input == "C":
                index = input("Enter the number of a song to mark as learned: ").strip()
                if not index.isdigit():
                    print("Invalid input; enter a valid number")
                    continue
                index = int(index)
                self.complete_song(index)
            else:
                print("Invalid menu choice")
            print(MENU)
            user_input = input(">>>").upper()


        print("Have a nice day :)")
        self.update_csv(file_path)
        print(f"{len(self.songs)} songs saved to {file_path}")



if __name__ == "__main__":
    songs_app = Run()
    songs_app.run()

