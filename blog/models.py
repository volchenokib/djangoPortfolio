from django.db import models

# Create a blog models.
# title
# pub_date
# body
# image


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add the blog app to the srttings

# Create a migration

# Migrate

# Add to the admin
