from .models import Question
from django import forms

class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget = forms.Textarea, label='')
    option1 = forms.CharField(label='')
    option2 = forms.CharField(label='')
    option3 = forms.CharField(label='')
    option4 = forms.CharField(label='')
    answer = forms.CharField(label='')
    marks = forms.IntegerField(label='')
    negative = forms.IntegerField(label='')
    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks', 'negative']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'Question'})
        self.fields['option1'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'option1'})
        self.fields['option2'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'option2'})
        self.fields['option3'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'option3'})
        self.fields['option4'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'option4'})
        self.fields['answer'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'answer'})
        self.fields['marks'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'marks'})
        self.fields['negative'].widget.attrs.update({'class' : 'w3-input w3-round', 'placeholder': 'negative'})