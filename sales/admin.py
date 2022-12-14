from django.contrib import admin
from .models import 아이디, Sale, Person

# Register your models here.

admin.site.register(아이디) # 모델에서 가져온다
admin.site.register(Sale)
admin.site.register(Person)