from django.contrib import admin
from .models import AllProduct,EachProductImage,Cart,Costumer,OrderPlaced


admin.site.register(AllProduct)
admin.site.register(EachProductImage)
admin.site.register(Costumer)
admin.site.register(Cart)
admin.site.register(OrderPlaced)