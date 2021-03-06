from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class users_app(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    screen_name = models.CharField(max_length=200, blank=True, null=True)
    statuses_count = models.IntegerField(default=0, blank=True, null=True)
    followers_count = models.IntegerField(default=0, blank=True, null=True)
    friends_count = models.IntegerField(default=0, blank=True, null=True)
    favourites_count = models.IntegerField(default=0, blank=True, null=True)
    listed_count = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    time_zone = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    default_profile = models.CharField(max_length=200, blank=True, null=True)
    default_profile_image = models.CharField(max_length=200, blank=True, null=True)
    geo_enabled = models.CharField(max_length=200, blank=True, null=True)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    profile_banner_url = models.CharField(max_length=200, blank=True, null=True)
    profile_use_background_image = models.CharField(max_length=200, blank=True, null=True)
    profile_background_image_url_https = models.CharField(max_length=500, blank=True, null=True)
    profile_text_color = models.CharField(max_length=200, blank=True, null=True)
    profile_image_url_https = models.CharField(max_length=200, blank=True, null=True)
    profile_sidebar_border_color = models.CharField(max_length=200, blank=True, null=True)
    profile_background_tile = models.CharField(max_length=200, blank=True, null=True)
    profile_sidebar_fill_color = models.CharField(max_length=200, blank=True, null=True)
    profile_background_image_url = models.CharField(max_length=200, blank=True, null=True)
    profile_background_color = models.CharField(max_length=200, blank=True, null=True)
    profile_link_color = models.CharField(max_length=200, blank=True, null=True)
    utc_offset = models.CharField(max_length=200, blank=True, null=True)
    protected = models.CharField(max_length=200, blank=True, null=True)
    verified = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)
    dataset = models.CharField(max_length=5, blank=True, null=True)
    bot = models.NullBooleanField(default=None)


class tweets_app(models.Model):
    created_at = models.CharField(max_length=200, blank=True, null=True)
    id = models.BigIntegerField(default=0, primary_key=True)
    text = models.CharField(max_length=1000, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.IntegerField(default=0, blank=True, null=True)
    truncated = models.CharField(max_length=200, blank=True, null=True)
    in_reply_to_status_id = models.BigIntegerField(default=0, blank=True, null=True)
    in_reply_to_user_id = models.BigIntegerField(default=0)
    in_reply_to_screen_name = models.CharField(max_length=200)
    retweeted_status_id = models.BigIntegerField(default=0, blank=True, null=True)
    geo = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    retweet_count = models.IntegerField(default=0, blank=True, null=True)
    reply_count = models.IntegerField(default=0, blank=True, null=True)
    favorite_count = models.IntegerField(default=0, blank=True, null=True)
    num_hashtags = models.IntegerField(default=0, blank=True, null=True)
    num_urls = models.IntegerField(default=0, blank=True, null=True)
    num_mentions = models.IntegerField(default=0, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    bot = models.NullBooleanField(default=None)


class links_app(models.Model):
    source_id = models.IntegerField(default=0)
    target_id = models.IntegerField(default=0)
    bot = models.BooleanField(default=None)


class friends_app(models.Model):
    source_id = models.IntegerField(default=0, blank=True, null=True)
    target_id = models.IntegerField(default=0, blank=True, null=True)
    bot = models.NullBooleanField(default=None)


class followers_app(models.Model):
    source_id = models.IntegerField(default=0, blank=True, null=True)
    target_id = models.IntegerField(default=0, blank=True, null=True)
    bot = models.NullBooleanField(default=None)


class sentiment_app(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    positive = models.IntegerField(default=0, blank=True, null=True)
    neutral = models.IntegerField(default=0, blank=True, null=True)
    negative = models.IntegerField(default=0, blank=True, null=True)
    bot = models.NullBooleanField(default=0)


