from django.db import models

# Create your models here.
class Template(models.Model):
    """Шаблон для печатной продукции."""
    template_name = models.CharField(max_length=200)
    template_description = models.CharField(max_length=200)
    template_data = models.ImageField(upload_to=None)

    def __str__(self) -> str:
        """Возвращает строковое представление модели в виде наименования шаблона."""
        return self.template_name


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.name


class PrintProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='print_products/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    product = models.ForeignKey(PrintProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}'s order for {self.product.name}"
