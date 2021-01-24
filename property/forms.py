from django import forms
from .models import RoomBook,RoomReview
class BookForm(forms.ModelForm):
    from_date=forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    to_date=forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model=RoomBook
        fields ='__all__'
        exclude=['room',]
class roomreviewform(forms.ModelForm):
    class Meta:
        model=RoomReview
        fields=['eat_rate','cleaning_rate','rate','feedback']
