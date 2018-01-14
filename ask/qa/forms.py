from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text.strip() == "":
            raise forms.ValidationError("Not be empty", code="Error1")
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text.strip() == "":
            raise forms.ValidationError("Not be empty", code="Error11")
        return text

    def clean_question(self):
        id = self.cleaned_data["question"]
        try:
            question = Question.objects.get(id=id)
        except Question.DoesNotExist:
            raise forms.ValidationError("Not question", code="Error2")
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
