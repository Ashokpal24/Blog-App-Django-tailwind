import json
import os
from os import listdir
# from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from author.models import Author
from tag.models import Tag
from blog.models import Blog
from comment.models import Comment
from shutil import copy

# Image list
# [
#     'The_Role_of_Science_in_Solving_Global_Challenges.jpg', 
#     'How_Technology_is_Changing_Education.jpg', 
#     'Top_Tech_Innovations_in_2024.jpg', 
#     'The_Science_Behind_Healthy_Living.jpg', 
#     'The_Future_of_Artificial_Intelligence.jpg', 
#     'Exploring_the_World_of_Digital_Art.jpg', 
#     'How_to_Stay_Healthy_in_a_Fast-Paced_World.png', 
#     'How_Artists_Are_Adapting_to_a_Digital_World.jpg', 
#     'Art_in_the_Age_of_Technology.jpg', 
#     'Health_Trends_to_Watch_in_2024.jpg'
# ]
 
class Command(BaseCommand):
    help = 'Create dummy data'

    def handle(self, *args, **kwargs):
        # load json data 
        with open('/workspaces/codespaces-blank/blog_app/blog/management/dummy_data.json','r') as f:
            json_data=json.load(f)

        image_path="/workspaces/codespaces-blank/blog_app/static/images_temp/"
        tag_list=['Technology', 'Science', 'Health', 'Education', 'Art']
        image_obj={}

        # create hashmap to store the extension [.jpg,.png]
        for file_name in listdir(image_path):
            name,extension=file_name.split('.')
            image_obj[name]=extension

        users={}

        # create user and author data-points in tables accordingly
        for user_data in json_data['users']:
            user=User.objects.create_user(
                username=user_data['username'],
                password=user_data['password']
            )
            author=Author.objects.create(user=user,bio=user_data['bio'])
            users[user_data['username']]=author

        tags={}

        # create tag data-points in tables accordingly
        for tag_name in tag_list:
            tag=Tag.objects.create(name=tag_name)
            tags[tag_name]=tag

        blogs={}
        # create blog data-points in tables accordingly
        # featured_image field is currenlty storing path at which images are copied

        for blog_data in json_data['blogs']:
            file_name=blog_data['title'].replace(" ","_")
            file_name+="."+image_obj[file_name]

            user_image_folder='static/images/blog_featured/user_{0}/'.format(blog_data["author"])

            # if generated path and content in it does not exists
            if os.path.exists(user_image_folder+file_name)==False:
                os.makedirs(user_image_folder, exist_ok=True)
                copy(image_path+file_name,user_image_folder+file_name)
            
            blog=Blog.objects.create(
                title=blog_data["title"],
                content=blog_data["content"],
                author=users[blog_data["author"]],
                featured_image=user_image_folder+file_name,
                is_published=True if blog_data["title"]!="The Future of Artificial Intelligence" else False
            )
            blog_tag_list=[tags[tag_name] for tag_name in blog_data['tags']]
            blog.tags.add(*blog_tag_list)
            blog.save()
            blogs[blog_data['title']]=blog
        
        for comment_data in json_data["comments"]:
            blog=blogs[comment_data["blog"]]
            author=users[comment_data["author"]]
            Comment.objects.create(
                blog=blog,
                author=author,
                content=comment_data['content'],
                is_approved=False if (
                    comment_data["blog"]=="How Artists Are Adapting to a Digital World" 
                    and 
                    comment_data["author"]=="bob_marley"
                    ) else True
            )
        print(f"Created {len(users)} users, {len(tags)} tags, {len(blogs)} blogs, and {len(json_data['comments'])} comments.")