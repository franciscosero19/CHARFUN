# Se han importado las librerías necesarias para el testeo

import unittest
import charfun

# Creación de la clase para testing

class TestCharfun(unittest.TestCase):

# Método para comprobar si el resultado de esPalindromo es igual a True o False

    def test_espalindromo(self):
        self.assertEqual(charfun.esPalindromo("Anita lava la tina"), True)
        self.assertEqual(charfun.esPalindromo("ANITA LAVA LA TINA"), True)
        self.assertEqual(charfun.esPalindromo("anita lava la tina."), True)
        self.assertEqual(charfun.esPalindromo("12222Anita 2113lava..,,,.la---tina"), True)
        self.assertEqual(charfun.esPalindromo(""), False)
        self.assertEqual(charfun.esPalindromo("Esta frase no es un palindromo"), False)