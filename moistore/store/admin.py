# moistore/store/admin.py
from django.contrib import admin
from .models import Category, Product  # Order can be added later when defined
from .models import CartItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
#admin.site.register(Movie)
#admin.site.register(Order)


