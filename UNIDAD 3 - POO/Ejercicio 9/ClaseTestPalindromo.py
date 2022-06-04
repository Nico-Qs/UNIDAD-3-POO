from ClasePalindromo import Palindromo
import unittest
class TestPalindromo(unittest.TestCase):
    __palabra: Palindromo
    def setUp(self):
        self.__palabra = Palindromo("MENEM")
    def test_esPalind(self):
        self.assertTrue(self.__palabra.esPalindromo())

