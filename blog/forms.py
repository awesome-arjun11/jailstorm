from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,max_length=50)
    contact_number = forms.CharField(max_length=15)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
	
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_number'].label = "Mobile No.:"
        self.fields['contact_email'].label = "Email Address:"
        self.fields['content'].label = "Message"

