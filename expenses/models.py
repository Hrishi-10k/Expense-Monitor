from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

POSITIVE_AMOUNT = [MinValueValidator(Decimal('0.01'))]


class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
    )
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'], name='unique_category_per_user'
            ),
        ]

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expenses',
    )
    # PROTECT: a category that still has expenses can never be deleted by accident.
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=POSITIVE_AMOUNT
    )
    description = models.TextField()
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-expense_date', '-id']

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"


class Budget(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='budgets',
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    monthly_limit = models.DecimalField(
        max_digits=10, decimal_places=2, validators=POSITIVE_AMOUNT
    )

    class Meta:
        ordering = ['category__name']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'category'], name='unique_budget_per_category'
            ),
        ]

    def __str__(self):
        return f"{self.category} - ₹{self.monthly_limit}"
