import unittest
from statement_builder import Rental_statement_builder
from regular_movies import Regular_movie

class VideoStoreTest(unittest.TestCase):
    def test_for_one_regualar_movie_incremental_rental_days(self):
        self.assertEqual(Rental_statement_builder('Regular Movie', 1, 0), '$2.0')
        self.assertEqual(Rental_statement_builder('Regular Movie', 1, 3), '$3.5')
        self.assertEqual(Rental_statement_builder('Regular Movie', 1, 4), '$5.0')
    
    def test_for_multiple_regular_movies_incremetal_rental_days(self):
        self.assertEqual(Rental_statement_builder('Regular Movie', 2, 0), '$4.0')
        self.assertEqual(Rental_statement_builder(movie = 'Regular Movie', number_of_movies = 3, number_of_days = 0), '$6.0')
        self.assertEqual(Rental_statement_builder('Regular Movie', 2, 7), '$19.0')

# TODO: get the tests passing with new classes (look at the arguments)



if __name__ == "__main__":
    unittest.main()  


# pass in rentals, give back statement. 
# data types: number of days(1-3), type of movie (regular, new release, childrens) 
# and the associated cost 
# frequent rental points based on number of days 
# Reg Movies: $2 for first 2 days, then $1.5 after  1.5*5 + $2 = 9.5

# classes: 
# do one class for each type of movie 
# one class to call those and spit out the statement 

# Rental Record for Customer Name
#   Crazynotes  £2.0
#   Teeth  £2.0
#   The Web  £3.5
# You owe £7.5
# You earned 3 frequent renter points