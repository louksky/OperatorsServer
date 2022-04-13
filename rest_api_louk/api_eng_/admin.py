from django.contrib import admin
from .models import FormulaHistory

@admin.register(FormulaHistory)
class FormulaHistoryAdmin(admin.ModelAdmin):
    list_display = ('is_done', 'created_at', 'result', 'operator', 'val1', 'val2' )
    search_fields = ['user__email', 'user__phone', 'operator','result', ]
    list_filter = ('is_done', 'result',)
    class Meta:
        verbose_name = "Formula History"
        verbose_name_plural = "Formulas History"
    pass