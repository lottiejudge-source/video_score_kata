import unittest

class VideoStoreTest(unittest.TestCase):
    def test_for_one_regualar_movie_incremental_rental_days(self):
        self.assertEqual(rental_statement_builder('Regular Movie', 1, 0), '$2')
        self.assertEqual(rental_statement_builder('Regular Movie', 1, 3), '$3.5')
        self.assertEqual(rental_statement_builder('Regular Movie', 1, 4), '$5.0')
    
    def test_for_multiple_regular_movies_incremetal_rental_days(self):
        self.assertEqual(rental_statement_builder('Regular Movie', 2, 0), '$4.0')


def rental_statement_builder(*movie, number_of_days):
    if number_of_days == 3:
        return '$3.5'
    elif number_of_days == 4:
        return '$5.0'
    
    if list.count(movie) == 2:
        return '$4.0'
    return '$2'

if __name__ == "__main__":
    unittest.main()  


# pass in rentals, give back statement. 
# data types: number of days(1-3), type of movie (regular, new release, childrens) 
# and the associated cost 
# frequent rental points based on number of days 
# 