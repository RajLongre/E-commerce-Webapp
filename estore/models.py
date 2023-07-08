from django.db import models
from django.contrib.auth.models import User




CATEGORY_CHOICES=(
    ("MensShirt","MensShirt"),
    ("MensTshirt","MensTshirt"),
    ("MensShoe","MensShoe"),
    ("WomensJacket","WomensJacket"),
    ("WomensSaree","WomensSaree"),
    ("KidsToy","KidsToy"),
    
)
class AllProduct(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="allproduct")
    price=models.FloatField()
    available=models.IntegerField()
    desc=models.TextField()
    category=models.CharField(max_length=30,choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name
    

class EachProductImage(models.Model):
    product=models.OneToOneField(AllProduct,on_delete=models.CASCADE,primary_key=True,related_name="allproduct")  
    image1=models.ImageField(upload_to="allproduct")
    image2=models.ImageField(upload_to="allproduct")
    def __str__(self) -> str:
        return str(self.product)
    


class Costumer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)
    
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(AllProduct,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)
    

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    costumer=models.ForeignKey(Costumer,on_delete=models.CASCADE)
    product=models.ForeignKey(AllProduct,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)

    

    

    