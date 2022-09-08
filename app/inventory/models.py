from django.db import models

class Product(models.Model):
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    pd_name = models.CharField(max_length=255)
    pd_description = models.TextField(blank=True)
    pd_price = models.DecimalField(max_digits=10, decimal_places=2)
    pd_create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    cl_name = models.CharField(max_length=255)
    cl_dni = models.IntegerField(default=0)
    cl_address = models.TextField(blank=True)
    cl_phone = models.CharField(max_length=255)
    cl_email = models.CharField(max_length=255)
    cl_create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BranchOffice(models.Model):
    class Meta:
        db_table = 'branch_office'
        verbose_name = 'Branch Office'
        verbose_name_plural = 'Branch Offices'

    bo_name = models.CharField(max_length=255)
    bo_nit= models.IntegerField(default=0)
    bo_address = models.TextField(blank=True)
    bo_phone = models.CharField(max_length=255)
    bo_email = models.CharField(max_length=255)
    bo_create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    class Meta:
        db_table = 'inventory'
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'

    inv_date = models.DateTimeField(auto_now_add=True)
    inv_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inv_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    inv_branch_office = models.ForeignKey(BranchOffice, on_delete=models.CASCADE)
    inv_quantity = models.IntegerField(default=0)
    inv_price = models.DecimalField(max_digits=10, decimal_places=2)
    inv_create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name