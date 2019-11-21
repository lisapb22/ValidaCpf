import unittest
from cpf import limparString, verificarTamanho
from ValidaCpf import CPF_Valido
class MyTest(unittest.TestCase):
    def test_limparString(self):
        self.assertEqual(limparString('123.123.133-33'), '12312313333')
        self.assertEqual(limparString('12312313333'), '12312313333')
        self.assertEqual(limparString('123 12..3--13-333'), '12312313333')
        self.assertEqual(limparString(''), '')
        self.assertEqual(limparString('-- -- '), '')
    
    def test_verificarTamanho(self):
        self.assertEqual(verificarTamanho('123.123.133-33'), True)
        self.assertEqual(verificarTamanho('12312313333'), True)
        self.assertEqual(verificarTamanho(''), False)
        self.assertEqual(verificarTamanho('123.123.13-33'), False)
        self.assertEqual(verificarTamanho('123.123.1223-33'), False)

    def test_cpfvalido(self):
        self.assertEqual(CPF_Valido("123.123.123-33"),False)
        self.assertEqual(CPF_Valido(""),False)
        self.assertEqual(CPF_Valido("0"),False)
        self.assertEqual(CPF_Valido("banana"),False)
        self.assertEqual(CPF_Valido("11111111111"),False)
        self.assertEqual(CPF_Valido("719.196.680-71"),True)
        self.assertEqual(CPF_Valido("333.333.333-33"),False)
        self.assertEqual(CPF_Valido("936.827.869-53"),True)

if __name__ == '__main__':
    unittest.main()