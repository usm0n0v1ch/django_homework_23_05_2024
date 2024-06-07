from django.contrib import admin

from myapp.models import Person, Child, IceCream, IceCreamKiosk

# Register your models here.
admin.site.register(Person)
admin.site.register(Child)
admin.site.register(IceCream)
admin.site.register(IceCreamKiosk)