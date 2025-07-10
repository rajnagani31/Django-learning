from django.db import models


class underConstruction(models.Model):
    is_under_construction = models.BooleanField(default=False)
    Uc_note = models.TextField(
        blank=True, null=True, help_text="Note for underconstruction mode"
    )
    uc_duration = models.DateTimeField(
        blank=True, null=True, help_text="END date and Time for under construction"
    )
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Under construction :{self.is_under_construction}"
