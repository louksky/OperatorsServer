from django.db import models
from django.conf import settings


class FormulaHistory(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    val1 = models.TextField(blank=True, default='')
    val2 = models.TextField(blank=True, default='')
    operator = models.TextField(blank=True, default='')
    result = models.TextField(blank=True, default='')
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return "formula: "+ self.formula +" done: "+ 'yes' if self.is_done else 'no'
    
    class Meta:
        ordering = ['created_at']
