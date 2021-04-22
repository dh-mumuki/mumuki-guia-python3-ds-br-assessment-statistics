class Test(unittest.TestCase):

  def test_deve_repetir_2_vezes(self):
    self.assertEqual(repete('Aa', 2), 'AaAa')

  def test_deve_repetir_5_vezes_por_padrao(self):
    self.assertEqual(repete('Aa'), 'AaAaAaAaAa')