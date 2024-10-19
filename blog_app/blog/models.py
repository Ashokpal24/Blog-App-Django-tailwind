from django.db import models
from tag.models import Tag
from author.models import Author

def user_directory_path(instance,filename):
    return f'images/blog_featured/user_{0}/{1}'.format(instance.user.id,filename)

class Blog(models.Model):
    title=models.CharField(blank=False,max_length=255)
    context=models.TextField()
    tags=models.ManyToManyField(Tag,related_name="articles",blank=True)
    author=models.ForeignKey(Author,related_name="articles",on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    published_at=models.DateField(null=True,blank=True)
    is_published=models.BooleanField(default=False)
    featured_image=models.ImageField(upload_to=user_directory_path)
    #slug

    def __str__(self) -> str:
        return f"{0} by {1}".format_map(self.title,self.author.user.username)