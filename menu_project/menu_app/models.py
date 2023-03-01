from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Menu title')
    create_at_menu = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.title


class CategoriesMenu(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    create_at_category = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
