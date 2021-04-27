from django.contrib import admin

# Register your models here.
from .models import Name
admin.site.register(Name)

from .models import Address
admin.site.register(Address)

from .models import Age
admin.site.register(Age)

from .models import Email
admin.site.register(Email)