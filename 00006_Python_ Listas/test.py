class Test(unittest.TestCase):

  def test_retorna_96374865_se_argumento_e_lista(self):
    lista = [1, 2, 3, 4, 'string', 'aluno', 4.2, 5, 96374849, True]
    self.assertEqual(soma_int(lista), 96374865, 'Deve retornar 96374865 se o argumento é a variável lista.')