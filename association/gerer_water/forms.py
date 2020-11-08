
from django import forms
from .models import Sasion
class SaisonForm(forms.ModelForm):
    class Meta:
        model =Sasion
        fields = ('annne',)

        labels = {
            'annne': "السنة الإستهلاكية",
        }

    def __init__(self, *args, **kwargs):
        super(SaisonForm, self).__init__(*args, **kwargs)
        self.fields['annne'].widget.attrs['min'] = 2020
        self.fields['annne'].widget.attrs['readonly'] = True
        self.fields['annne'].initial = 2020



def getLastSaison():
    last_year=Sasion.objects().all().reverse()[0] if Sasion.objects().count()>0 else 2020
    return last_year

