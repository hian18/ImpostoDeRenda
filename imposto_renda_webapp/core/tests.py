from django.test import Client
from django.test import SimpleTestCase


class TestCalculoImpostRenda(SimpleTestCase):
    def __init__(self, *args, **kwargs):
        import os
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'imposto_renda_webapp.settings')
        django.setup()
        super().__init__(*args, **kwargs)

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

    def test_calculo_salario_30000(self):
        c = Client()
        post_data = dict(salario_anual=30000)
        response = c.post('/calcular-imposto-renda', post_data)
        self.assertNotEqual("Isento!", response.content.decode())
