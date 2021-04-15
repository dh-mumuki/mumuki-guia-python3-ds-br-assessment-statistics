class Test(unittest.TestCase):

  def test_somar_3_depois_de_dobrar_7_resulta_17(self):
    f = lambda x: 2*x
    g = lambda x: x + 3
    
    self.assertEqual(composicao(7,f,g), 17)
    
  def test_raiz_quadrada_depois_de_dividir_128_por_2_rsulta_8(self):
    from math import sqrt
    f = lambda x: x/2
    g = lambda x: sqrt(x)
    
    self.assertAlmostEqual(composicao(128,f,g), 8)