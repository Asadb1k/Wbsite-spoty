from django.db import models




class NameMod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class SingMod(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    photo = models.FileField(upload_to='photo')
    file = models.FileField(upload_to='sing')
    category = models.ForeignKey(to=NameMod,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

class CommentMod(models.Model):
    username = models.CharField(max_length=50)
    comment = models.TextField()
    song_author = models.CharField(max_length=70)
    

