class TestFixtures(unittest.TestCase):
  def test_se_argumento_14_retorna_3(self):
    self.assertEquals(condicional(14), 3)
      
  def test_se_argumento_menos_11_retorna_784(self):
    self.assertEquals(condicional(-11), 784)
  
  def test_se_argumento_22_retorna_25(self):
    self.assertEquals(condicional(22), 25)