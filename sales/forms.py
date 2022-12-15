from django import forms
from .models import Sale

class SaleModelForm(forms.ModelForm): # 모델폼은 아래 일반 폼과 다르게 필드를 지정할 필요가 없다(대신 메타 클래스를 지정함)
    class Meta:
        model = Sale
        fields = (
            'first_name',
            'last_name',
            'age',
            'person',
        )

class SaleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)