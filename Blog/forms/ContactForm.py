from django import forms

from Blog.models.Contact import Contact


class ContactForm(forms.ModelForm):
    CIVILITY_CHOICES = (
        ('M.', 'Monsieur'),
        ('Mme.', 'Madame'),
    )
    civility = forms.ChoiceField(choices=CIVILITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Contact
        fields = ('civility', 'name', 'email', 'subject', 'message', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
