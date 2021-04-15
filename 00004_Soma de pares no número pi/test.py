class Test(unittest.TestCase):

  def test_retorna_48_se_argumento_e_10(self):
    self.assertEqual(soma_pares_em_pi(10), 48, 'Deve retornar 48 se o argumento é 10.')

  def test_retorna_5166_se_argumento_e_1251(self):
    self.assertEqual(soma_pares_em_pi(1251), 5166, 'Deve retornar 5166 se o argumento é 1251.')