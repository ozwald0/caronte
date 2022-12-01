from django.urls import path
from . import views
from .views import GeneratePDF, GeneratePDFService, GeneratePDFComplete 

urlpatterns = [
    #Enlace principal
    path("", views.index, name = "index"),
    path("index/", views.index, name = "index"),
    # Enlaces del index
    path("services/", views.services, name = "services"),
    path("users/", views.users, name = "users"),
    path("clients/", views.clients, name = "clients"),
    path("items/", views.items, name = "items"),
    path("service_status/", views.service_status, name = "service_status"),
    path("reports/", views.reports, name = "reports"),
    path("client_view/", views.client_view, name = "client_view"),
    path("home/", views.home, name = "home"),
    path("login_user/", views.login_user, name = "login_user"),
    #Enlaces de Services
    path("services/new_service", views.new_service, name = "new_service"),
    path("services/service_detail/<int:service_id>", views.service_detail, name = "service_detail"),
    path("services/update_service/<int:service_id>", views.update_service, name = "update_service"),
    #path("r'^pdf/$", GeneratePDF.as_view()),
    #path("item_pdf", GeneratePDF.as_view(), name="item_pdf"),
    path("GeneratePDF/<int:service_id>", GeneratePDF.as_view(), name="GeneratePDF"),
    path("GeneratePDFService/<int:service_id>", GeneratePDFService.as_view(), name="GeneratePDFService"),
    path("GeneratePDFComplete/<int:service_id>", GeneratePDFComplete.as_view(), name="GeneratePDFComplete"),
    #Status de Servicio
    path("service_status/new_service_status", views.new_service_status, name = "new_service_status"),
    #Enlaces de clients

    path("clients/new_client/", views.new_client, name = "new_client"),
    path("clients/client_detail/<int:client_id>", views.client_detail, name = "client_detail"),
    path("clients/update_client/<int:client_id>", views.update_client, name = "update_client"),
    path("clients/update_client/service_detail/<int:service_id>/", views.service_detail, name = "service_detail"),
    path("clients/client_detail/service_detail/<int:service_id>/", views.service_detail, name = "service_detail"),
    #Enlaces de users
    path("users/new_user/", views.new_user, name = "new_user"),
    path("users/user_detail/<int:user_id>", views.user_detail, name = "user_detail"),
    #Enlaces de home
    path("home/service_detail/<int:service_id>", views.service_detail, name = "service_detail"),
    path("home/new_service", views.new_service, name = "new_service"),
    path("home/update_service/<int:service_id>", views.update_service, name = "update_service"),
    #Enlaces de login/logout
    path("login_user/home/", views.home, name = "home"),
    #Enlaces de items/new item
    path("items/new_item/", views.new_item, name = "new_item"),
    path("items/new_item/new_type_of_item", views.new_type_of_item, name = "new_type_of_item"),
    #Enlaces de client_view
    path("client_view/client_view_detail/<int:client_id>", views.client_view_detail, name = "client_view_detail"),
    path("", views.client_view_detail, name = "client_view_detail"),
    #enlaces de reportes
    path("reports/service_detail/<int:service_id>/", views.service_detail, name = "service_detail"),


]
    # enlaces depreciados
        #
        #path("status_of_user/", views.status_of_user, name = "status_of_user"),
        #path("levels/new_level/", views.new_level, name = "new_level"),
        #path("user_status/", views.user_status, name = "user_status"),
        #path("<int:client_id>/", views.index, name = "index"),
        #path("<int:item_id>/", views.index, name = "index"),