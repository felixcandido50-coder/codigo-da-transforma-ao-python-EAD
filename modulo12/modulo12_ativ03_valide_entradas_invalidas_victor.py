import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

class TestValidaEntradas(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero_lanca_excecao(self):
        with self.assertRaises(ValueError) as contexto:
            self.calc.dividir(10, 0)
        
        self.assertEqual(str(contexto.exception), "Divisão por zero não é permitida.")

if __name__ == '__main__':
    unittest.main()