class TestFixtures(unittest.TestCase):
  def test_se_argumento_14_retorna_3(self):
    self.assertEqual(condicional(14), 3)
      
  def test_se_argumento_menos_11_retorna_menos_6(self):
    self.assertEqual(condicional(-11), -6)
  
  def test_se_argumento_22_retorna_25(self):
    self.assertEqual(condicional(22), 25)