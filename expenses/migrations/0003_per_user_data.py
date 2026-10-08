from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def assign_existing_rows(apps, schema_editor):
    """Give rows created before per-user support to the first user.

    If there are no users at all, the orphan rows cannot belong to anybody
    and are removed. Duplicate budgets (possible through the old edit form)
    are collapsed so the new unique constraint can be applied.
    """
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    Category = apps.get_model('expenses', 'Category')
    Expense = apps.get_model('expenses', 'Expense')
    Budget = apps.get_model('expenses', 'Budget')

    first_user = User.objects.order_by('id').first()
    if first_user is None:
        Expense.objects.all().delete()
        Budget.objects.all().delete()
        Category.objects.all().delete()
        return

    Category.objects.filter(user__isnull=True).update(user=first_user)
    Expense.objects.filter(user__isnull=True).update(user=first_user)
    Budget.objects.filter(user__isnull=True).update(user=first_user)

    seen = set()
    for budget in Budget.objects.order_by('id'):
        if budget.category_id in seen:
            budget.delete()
        else:
            seen.add(budget.category_id)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0002_alter_category_name'),
    ]

    operations = [
        # Names are now unique per user instead of globally.
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(assign_existing_rows, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='expenses.category'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='budget',
            name='monthly_limit',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-expense_date', '-id']},
        ),
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ['category__name']},
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique_category_per_user'),
        ),
        migrations.AddConstraint(
            model_name='budget',
            constraint=models.UniqueConstraint(fields=('user', 'category'), name='unique_budget_per_category'),
        ),
    ]
