from operator import truediv
from django.db import models

# Create your models here.


class Candidate(models.Model):
    candidate_username = models.CharField(
        max_length=200, null=True, blank=True, default="")

    candidate_name = models.CharField(
        max_length=200, null=True, blank=True, default="")

    candidate_avatar_url = models.URLField(
        max_length=200, null=True, blank=True, default="")

    candidate_url = models.URLField(
        max_length=200, null=True, blank=True, default="")

    candidate_company = models.CharField(
        max_length=200, null=True, blank=True, default="")

    candidate_blog_url = models.URLField(
        max_length=200, null=True, blank=True, default="")

    candidate_location = models.CharField(
        max_length=200, null=True, blank=True, default="")

    candidate_email = models.CharField(
        max_length=200, null=True, blank=True, default="")

    candidate_bio = models.CharField(
        max_length=400, null=True, blank=True, default="")

    candidate_repo_number = models.IntegerField(
        null=True, blank=True, default="")

    candidate_gists_number = models.IntegerField(
        null=True, blank=True, default="")

    candidate_follower_number = models.IntegerField(
        null=True, blank=True, default="")

    candidate_following_number = models.IntegerField(
        null=True, blank=True, default="")

    candidate_join_date = models.CharField(
        max_length=100, null=True, blank=True, default="")

    candidate_notes = models.CharField(
        max_length=1000, null=True, blank=True, default="")

    stackoverflow_candidate_name = models.CharField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_url = models.URLField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_avatar_url = models.URLField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_blog_url = models.URLField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_location = models.CharField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_bio = models.CharField(
        max_length=400, null=True, blank=True, default="")

    stackoverflow_candidate_view_count = models.CharField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_up_vote_count = models.CharField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_answer_count = models.CharField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_question_count = models.CharField(
        max_length=200, null=True, blank=True, default="")

    stackoverflow_candidate_reputation = models.CharField(
        max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return self.candidate_name
