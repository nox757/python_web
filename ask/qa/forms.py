from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text.strip() == "":
            raise forms.ValidationError("Not be empty", code="Error_empty")
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text.strip() == "":
            raise forms.ValidationError("Not be empty", code="Error_empty")
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
        answer.author_id = self._user.id
        answer.save()
        return answer


#not released safety password with hash
class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username.strip() == '':
            raise forms.ValidationError("Not be empty", code='error_empty')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Username already exist", code="error_exist")
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email.strip() == '':
            raise forms.ValidationError("Not be empty", code="error_empty")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if password.strip() == '':
            raise forms.ValidationError("Not be empty", code="error_empty")
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username.strip() == '':
            raise forms.ValidationError("Not be empty", code='error_empty')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Username already exist", code="error_exist")
        except User.DoesNotExist:
            pass
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        if password.strip() == '':
            raise forms.ValidationError("Not be empty", code="error_empty")
        return password

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Not valid user/login", code="error_auth")
        if not user.check_password(password):
            raise forms.ValidationError("Not valid user/login", code="error_auth")
