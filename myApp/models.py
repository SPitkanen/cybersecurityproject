from django import forms
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        app_label = 'myApp'

class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def get_upvote_count(self):
        return self.vote_set.filter(vote_type='up').count()
    class Meta:
        app_label = 'myApp'

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image', 'description']

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    text = models.TextField()
    class Meta:
        app_label = 'myApp'

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=4, choices=[('up', 'Upvote'), ('down', 'Downvote')])
    class Meta:
        app_label = 'myApp'
