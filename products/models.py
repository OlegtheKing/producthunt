from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField
    url = models.URLField
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.PositiveSmallIntegerField(default=1)
    image =  models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="icons/")
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)  # what happens when user deleted

    def summary(self):
        return self.body[:150] + "..."

    def pub_date_simple(self):
        return self.pub_time.strftime("%b %e %Y")

    def __str__(self):  # the name used whenever django-adm displays object
        return self.title

