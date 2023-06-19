from django import forms
from .models import Home

# class TestFormHome(forms.ModelForm):
    
#     class Meta:
#         model = Home
#         # fields = ('__all__')
#         fields = (
#             'title',
#             'subtitle',
#             'quantity',
#         )

#     def clean_quantity(self):
#         quantity = self.cleaned_data['quantity']
#         if quantity < 10:
#             raise forms.ValidationError('The number must be > 10')
#         return quantity

class TestFormHome(forms.ModelForm):
    
    class Meta:
        model = Home
        # fields = ('__all__')
        fields = (
            'title',
            'subtitle',
            'quantity',
        )
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'placeholder': 'Enter the text here'        
                }
            )
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 10:
            raise forms.ValidationError('The number must be > 10')
        return quantity