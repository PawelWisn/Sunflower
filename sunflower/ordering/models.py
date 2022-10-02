from django.db import models
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    email = models.EmailField(_("Email"), max_length=52)
    notes = models.TextField(_("Notes"),max_length=4000, default='')
    reviewed = models.BooleanField(_("Reviewed"), default=False)
    finished = models.BooleanField(_("Finished"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    picture = models.ImageField(_("Picture"), upload_to="")
    
    def __str__(self):
        return f"{self.id}: {self.picture}"
    
    class Meta:
        ordering = ["-created_at"]