# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def movie_info(self):
        print(f'{self.title} {self.director} {self.budget}')

    def was_expensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False


movie1 = Movie('Title: Avengers,', 'Director: Joe Russo, Budget:', 220000000)
movie1.movie_info()
print('Budget is more than 100M:', movie1.was_expensive())

movie2 = Movie('Title: Memory,', 'Director: Liam Neeson, Budget:', 30000000)
movie2.movie_info()
print('Budget is more than 100M:', movie2.was_expensive())

