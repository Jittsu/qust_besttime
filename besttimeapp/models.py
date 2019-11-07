from django.db import models
from django.core import validators

class Item(models.Model):

    DISTANCE_CHOICES = (
        (1, '50m'),
        (2, '100m'), 
        (3, '200m'),
        (4, '400m'),
        (5, '800m'),
        (6, '1500m'),
    )

    EVENT_CHOICES = (
        (1, '自由形'),
        (2, '背泳ぎ'),
        (3, '平泳ぎ'),
        (4, 'バタフライ'), 
        (5, '個人メドレー'),
    )

    kanji_name = models.CharField(
        verbose_name = '名前（漢字）',
        max_length = 10
    )

    hiragana_name = models.CharField(
        verbose_name = '名前（ひらがな）',
        max_length = 30
    )

    distance = models.IntegerField(
        verbose_name = '距離',
        choices = DISTANCE_CHOICES,
        default = 1
    )

    event = models.IntegerField(
        verbose_name = '種目',
        choices = EVENT_CHOICES,
        default = 1,
    )

    time_min = models.IntegerField(
        verbose_name = '分',
        default = 0
    )

    time_sec = models.DecimalField(
        verbose_name = '秒（小数点以下まで）',
        max_digits = 5,
        decimal_places = 2,
        default = 0.00
    )

    created_at = models.DateTimeField(
        verbose_name = '登録日',
        auto_now_add = True
    )

    memo = models.TextField(
        verbose_name = '備考',
        max_length = 300,
        blank = True,
        null = True
    )

    def __str__(self):
        return self.name
