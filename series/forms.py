from django import forms


from .models import Series

class AddForm(forms.ModelForm):

      class Meta:
         model = Series
         fields = ('__all__')

        #  widgets= {
        #     'title' : forms.TextInput(attrs={'class':'form-control'}),
        #     'description' : forms.TextInput(attrs={'class':'form-control'}),
        #     'image': forms.FileInput(attrs={'class': 'form-control'}),
        #     'image2': forms.FileInput(attrs={'class': 'form-control'}),
        #     'cost' : forms.TextInput(attrs={'class':'form-control'}),
        #     'characteristic' :forms.TextInput(attrs={'class':'form-control'}),
        #
        # }