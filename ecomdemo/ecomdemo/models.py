from django.db import models
class User(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50, choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], default='Mrs' )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    #id is not specified but in settings we have provided Default Auto Field which will create a primary key automatically.
    address = models.CharField(max_length=50, null=True)


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)# if user is deleted then the product will be deleted.
    #if we don't want to delete we can make on_delete=models.DO_NOTHING
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    stock = models.IntegerField()


