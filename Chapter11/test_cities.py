import unittest
from city_functions import get_country_city

class TestCityCountry(unittest.TestCase):
    def test_country_city(self):
        city_country = get_country_city('Beijing','China')
        self.assertEqual(city_country,"Beijing,China")

    def test_city_country_population(self):
        city_country_population = get_country_city('Beijing','China', population=22000000)
        self.assertEqual(city_country_population, "Beijing,China - population 22000000")
if __name__ == '__main__':
    unittest.main()
