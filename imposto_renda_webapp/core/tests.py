from django.test import SimpleTestCase
from django.test import Client
# Create your tests here.


class TestCalculoImpostRenda(SimpleTestCase):
    def test_calculo_salario_10000(self):
        c = Client()
        post_data = dict(salario_anual=10000)
        response = c.post('/calcular-imposto-renda', post_data)
        self.assertEqual("Isento!", response.content.decode())

    def test_calculo_salario_100000(self):
        c = Client()
        post_data = dict(salario_anual=100000)
        response = c.post('/calcular-imposto-renda', post_data)
        self.assertNotEqual("Isento!", response.content.decode())
