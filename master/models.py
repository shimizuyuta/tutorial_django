import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
 
class Employee(models.Model):
    """ 社員マスタ """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name = "名前", max_length=20,default='')
    name_furigana = models.CharField(verbose_name = "ふりがな", max_length=20,default='')
 
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$',
        message = (u"電話番号は半角英数のみで入力してください。例：09012345678"))
    tel_number = models.CharField(validators=[tel_number_regex],
        max_length=15, verbose_name='電話番号',blank=True, null=True)
 
    entering_date = models.DateTimeField(verbose_name = "入社日", blank=True, null=True)
    retirement_date = models.DateTimeField(verbose_name = "退職日", blank=True, null=True)
 
    created_date = models.DateTimeField(verbose_name = "作成日", default=timezone.now)
    published_date = models.DateTimeField(verbose_name = "更新日", blank=True, null=True)
 
    def save(self, *args, **kwargs):
        auto_now = kwargs.pop('published_date', True)
        if auto_now:
            self.published_date = timezone.now()
        super(Employee, self).save(*args, **kwargs)
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '社員'
        verbose_name_plural = '社員名簿'
