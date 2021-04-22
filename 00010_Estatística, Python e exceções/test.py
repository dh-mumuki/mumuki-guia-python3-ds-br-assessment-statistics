class Test(unittest.TestCase):

  def test_dois_eventos(self):
    pmf = [(6,0.8), (9,0.2)]
    self.assertAlmostEqual(expectativa(pmf), 6.6)
  
  def test_distribuicao_invalida(self):
    self.assertRaises(expectativa([]), ValueError)
  
  def test_dado_de_20_faces(self):
    n = 20
    pmf = zip(range(1, n+1), [round(1/n, 2)] * n)
    self.assertEqual(expectativa)