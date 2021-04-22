class Test(unittest.TestCase):

  def test_1_ocorre_3x(self):
    lista = [1,1,7,1]
    self.assertEqual(count(1, lista), 3)
    
  def test_string_ocorre_2x(self):
    lista = [3, 'a', 'a', 0, None]
    self.assertEqual(count('a', lista), 2)
  
  def test_lista_vazia(self):
    self.assertEqual(count(1 ,[]), 0, 'Deve retornar zero se a lista estiver vazia.')
  
  def test_nenhuma_ocorrencia(self):
    lista = [1,1,7,1]
    self.assertEqual(count(5, lista), 0, 'Deve retornar zero se o elemento não estiver na lista.')
    