from django.contrib import admin
from .models import Post, Category, Tag
from pagedown.widgets import AdminPagedownWidget
from django import forms


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category',
                    'author']
    form = PostForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
