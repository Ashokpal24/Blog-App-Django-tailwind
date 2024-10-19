from django.db import models
from author.models import Author
from blog.models import Blog

class Comment(models.Model):
    blog=models.ForeignKey(Blog,related_name="comments",on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    content=models.TextField()
    is_approved=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    likes=models.PositiveIntegerField(default=0)
    dislikes=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.author.user.name