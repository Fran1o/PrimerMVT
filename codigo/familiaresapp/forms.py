from django import forms

class FamiliaFormulario(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=30)

    fechanacimiento = forms.DateField()

    edad = forms.IntegerField()


class PrimosFormulario(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=30)

    fechanacimiento = forms.DateField()

    edad = forms.IntegerField()


class TiosFormulario(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=30)

    fechanacimiento = forms.DateField()

    edad = forms.IntegerField()

     