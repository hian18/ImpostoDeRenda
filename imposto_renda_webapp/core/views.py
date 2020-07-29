from django.shortcuts import render
from django.views import View
from django import forms
from django.http import HttpResponse
from imposto_renda.calculos import calcular_imposto_de_renda


class RendaUsuarioForm(forms.Form):
    salario_anual = forms.FloatField()
    nome = forms.CharField()


class ImpostoRendaView(View):
    form = RendaUsuarioForm

    def post(self, request, *args, **kwargs):
        form=self.form(request.POST)
        result = calcular_imposto_de_renda(float(form.data['salario_anual']))
        return HttpResponse(result)
