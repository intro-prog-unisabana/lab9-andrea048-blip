class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"


def main():
    title = input("Enter movie title:\n")
    director = input("Enter director:\n")
    year = int(input("Enter year:\n"))

    movie = Movie(title, director, year)
    print(movie)


if __name__ == "__main__":
    main()