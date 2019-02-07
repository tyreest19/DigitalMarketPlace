from django import forms
from .models import Product

PUBLISH_CHOICES = (
    ('publish', 'Publish'),
    ('draft', 'Draft')
)
class ProductAddForms(forms.Form):
    title = forms.CharField()
    description =  forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    publish = forms.ChoiceField(choices=PUBLISH_CHOICES)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 1.00:
            raise forms.ValidationError('Price Must be greater than 1')
        return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 2:
            return title
        else:
            raise forms.ValidationError('Title must be greater than 2')

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 1.00:
            raise forms.ValidationError('Price Must be greater than 1')
        return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 2:
            return title
        else:
            raise forms.ValidationError('Title must be greater than 2')
