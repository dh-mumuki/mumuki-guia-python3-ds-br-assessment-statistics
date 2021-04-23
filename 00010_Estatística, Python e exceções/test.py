class Test(unittest.TestCase):

    def test_dois_eventos(self):
        pmf = [(6,0.8), (9,0.2)]
        self.assertAlmostEqual(expectativa(pmf), 6.6)
  
    def test_eventos_nao_coletivamente_exaustivos(self):
        with self.assertRaises(ValueError, msg='Deve lançar exceção ValueError se os eventos não forem coletivamente exaustivos'):
            expectativa([(1, 0.5)])

    def test_distribuicao_invalida(self):
        with self.assertRaises(ValueError, msg='Deve lançar exceção ValueError se o argumento for []'):
            expectativa([])

    def test_dado_de_8_faces(self):
        pmf = zip(range(1, 9), [0.125] * 8)
        self.assertEqual(expectativa(pmf), 4.5, msg='Um dado honesto de 8 faces tem expectativa 4.5.')  