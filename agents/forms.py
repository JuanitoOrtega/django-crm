from leads.models import Agent
from django.forms import *


class AgentModelForm(ModelForm):

    class Meta:
        model = Agent
        fields = ('user',)
        widgets = {
            'user': Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }