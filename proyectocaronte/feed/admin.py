from django.contrib import admin
from .models import Client, Service, Item, ItemDetail, ServiceComment, ClientComment, TypeOfProduct, Status, TypeOfService, TypeOfItem

#admin.site.register(User)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Item)
admin.site.register(ItemDetail)
admin.site.register(ServiceComment)
admin.site.register(ClientComment)
admin.site.register(TypeOfProduct)
admin.site.register(Status)
admin.site.register(TypeOfService)
#admin.site.register(Level)
#admin.site.register(StatusOfUsers)
admin.site.register(TypeOfItem)

