from django import forms

class SendMessageForm(forms.Form):
    chat_id = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
