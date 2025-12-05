from regular_movies import Regular_movie
class Rental_statement_builder: 
    def __init__(self, type_of_movie, number_of_movies, number_of_days):
        self.type_of_movie = type_of_movie,
        self.number_of_movies = number_of_movies,
        self.number_of_days = number_of_days

    def rental_statement(self, movie, type_of_movie, number_of_movies, number_of_days):    
        if type_of_movie == "regular": 
           current_movie = Regular_movie()

        base_rate = current_movie.base_rate
        rental_period = number_of_days - 2 
        daily_rate = 1.5
        rental_total = base_rate + (daily_rate * rental_period)
        
        statement_total =  rental_total * number_of_movies

        if number_of_days <= 2:
            return f'${base_rate * number_of_movies}'
        else:
            return f'${statement_total}'
