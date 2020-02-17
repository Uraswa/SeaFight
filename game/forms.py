from django import forms


class GameLaunchForm(forms.Form):

    height = forms.IntegerField(max_value=32, min_value=1, required=True)
    width = forms.IntegerField(max_value=32, min_value=1, required=True)
    f1 = forms.IntegerField(min_value=0)
    f2 = forms.IntegerField(min_value=0)
    f3 = forms.IntegerField(min_value=0)
    f4 = forms.IntegerField(min_value=0)
    f5 = forms.IntegerField(min_value=0)
    f6 = forms.IntegerField(min_value=0)
