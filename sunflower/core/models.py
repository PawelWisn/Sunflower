from django.utils.translation import gettext_lazy as _
from django.db import models
from .constants import SMALL_SIZE, MEDIUM_SIZE, LARGE_SIZE


class Product(models.Model):
    """Represents sellable item"""

    SIZES = (
        (SMALL_SIZE, _("Small")),
        (MEDIUM_SIZE, _("Medium")),
        (LARGE_SIZE, _("Large")),
    )

    name = models.CharField(_("Name"), max_length=255)
    quantity = models.PositiveIntegerField(_("Quantity"))
    picture = models.ImageField(_("Image"), upload_to="images/stickers/", null=True)
    size = models.CharField(_("Size"), choices=SIZES, max_length=3, db_index=True)
    order = models.PositiveIntegerField(_("Order"), default=1, db_index=True)

    def __str__(self):
        return f"{self.name}: {self.get_size_display()}"

    class Meta:
        ordering = ("order", "name")
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
