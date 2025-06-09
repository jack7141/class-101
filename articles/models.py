from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from model_utils.models import UUIDModel, SoftDeletableModel, TimeStampedModel

from interaction.models import Comment, Like


# Create your models here.
class Article(UUIDModel, SoftDeletableModel, TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    comments = GenericRelation(Comment, related_query_name='article')
    likes = GenericRelation(Like, related_query_name='article')