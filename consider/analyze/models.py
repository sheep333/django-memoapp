from django.db import models


class Analyze(models.Model):
    """
    分析カードモデル。マルチ継承で他のテーブルを作成。
    """
    name = models.CharField(
        verbose_name='テンプレート名'
    )
    parent_id = models.IntegerField(
        verbose_name='親ID'
    )
    type_id = models.IntegerField(
        verbose_name='分析タイプ'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

class MemoAnalyze(Analyze):
    type_id = 0
    name = 'メモ型テンプレート'
    subject = models.CharField(
        verbose_name='件名',
        max_length=100,
        default='',
        blank=False,
    )
    body = models.TextField(
        verbose_name='本文',
        default='',
        blank=True
    )

    def __str__(self):
        return self.type_id

class QuestionAnalyze(Analyze):
    type_id = 1
    name = '質問型テンプレート'
    question = models.CharField(
        verbose_name='質問',
        max_length=100,
        default='',
        blank=False,
    )
    answer = models.TextField(
        verbose_name='答え',
        default='',
        blank=True
    )

    def __str__(self):
        return self.type_id

class FreeAnalyze(Analyze):
    type_id = 2
    name = '自由型テンプレート'
    content = models.TextField(
        verbose_name='テキスト',
        default='',
        blank=True,
    )

    def __str__(self):
        return self.type_id