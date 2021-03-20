from django import forms
from django.db.models import fields
from django.db.models.base import Model
from tinymce.widgets import TinyMCE
from .models import _your_model_
from blog.models import Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 50, 'rows': 30}
        )
    )

    class Meta:
        model = _your_model_
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)
