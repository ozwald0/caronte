from ast import Not
import datetime
from datetime import date, time
from http.client import HTTPResponse
from time import timezone
from unicodedata import name
from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from .models import Service, Client, Item, TypeOfItem, ItemDetail, Status, TypeOfService, TypeOfProduct, ServiceComment
from django.db.models import Q

from django.template.loader import get_template
#from django.http import FileResponse
#import io
#from reportlab.pdfgen import canvas
#from reportlab.lib.units import cm
#from reportlab.lib.pagesizes import letter
from .functions import render_to_pdf
from django.views.generic import View

#genergenerateate PDF File
class GeneratePDF(View):
    def get(self, request, service_id):
        template = get_template('feed/pdf_view.html')
        service = Service.objects.get(pk = service_id)
        client = Client.objects.get(id = service.client.id)
        all_item_details = ItemDetail.objects.filter(service = service_id)
        all_service_comments = ServiceComment.objects.filter(service = service_id)
        if service.is_working:
            working_si_no = "Si"
        else:
            working_si_no = "No"
        if service.is_damaged:
            damaged_si_no = "Si"
        else:
            damaged_si_no = "No"
        if service.is_complete:
            complete_si_no = "Si"
        else:
            complete_si_no = "No"
        context = {
            "service": service,
            "all_item_details": all_item_details,
            "client": client,
            "working_si_no": working_si_no,
            "damaged_si_no": damaged_si_no,
            "complete_si_no": complete_si_no,
        }
        html = template.render(context)
        pdf = render_to_pdf('feed/pdf_view.html', context)
        if pdf:
            return HttpResponse(pdf, content_type = 'application/pdf')
            #return HttpResponse(html)
            #return pdf
        return HTTPResponse("no hay pdf")


class GeneratePDFService(View):
    def get(self, request, service_id):
        template = get_template('feed/pdf_view_service.html')
        service = Service.objects.get(pk = service_id)
        client = Client.objects.get(id = service.client.id)
        all_item_details = ItemDetail.objects.filter(service = service_id)
        all_service_comments = ServiceComment.objects.filter(service = service_id)
        now = datetime.datetime.now()
        if service.is_working:
            working_si_no = "Si"
        else:
            working_si_no = "No"
        if service.is_damaged:
            damaged_si_no = "Si"
        else:
            damaged_si_no = "No"
        if service.is_complete:
            complete_si_no = "Si"
        else:
            complete_si_no = "No"
        context = {
            "service": service,
            "all_item_details": all_item_details,
            "client": client,
            "now": now,
            "working_si_no": working_si_no,
            "damaged_si_no": damaged_si_no,
            "complete_si_no": complete_si_no,
        }
        html = template.render(context)
        pdf = render_to_pdf('feed/pdf_view_service.html', context)
        if pdf:
            return HttpResponse(pdf, content_type = 'application/pdf')
            #return HttpResponse(html)
            #return pdf
        return HTTPResponse("no hay pdf")


class GeneratePDFComplete(View):
    def get(self, request, service_id):
        template = get_template('feed/pdf_view_complete.html')
        service_item_price = 0
        service = Service.objects.get(pk = service_id)
        client = Client.objects.get(id = service.client.id)
        all_item_details = ItemDetail.objects.filter(service = service_id)
        all_service_comments = ServiceComment.objects.filter(service = service_id)
        if service.is_working:
            working_si_no = "Si"
        else:
            working_si_no = "No"
        if service.is_damaged:
            damaged_si_no = "Si"
        else:
            damaged_si_no = "No"
        if service.is_complete:
            complete_si_no = "Si"
        else:
            complete_si_no = "No"
        for item in all_item_details:
            #service_full_price = service_full_price + item.price
            service_item_price = service_item_price + item.price
        service_price = service.service_price
        total_price = service_price + service_item_price
        item_number = all_item_details.count()
        now = datetime.datetime.now()
        context = {
            "service": service,
            "all_item_details": all_item_details,
            "client": client,
            "now": now,
            "service_price": service_price,
            "service_item_price": service_item_price,
            "total_price": total_price,
            "item_number": item_number,
            "working_si_no": working_si_no,
            "damaged_si_no": damaged_si_no,
            "complete_si_no": complete_si_no,
        }
        html = template.render(context)
        pdf = render_to_pdf('feed/pdf_view_complete.html', context)
        if pdf:
            return HttpResponse(pdf, content_type = 'application/pdf')
            #return HttpResponse(html)
            #return pdf
        return HTTPResponse("no hay pdf")

def index(request):
    return render(request, 'feed/index.html', {})


def services(request):
    all_services = Service.objects.all()      
    return render(request, 'feed/services.html', {
        "all" : all_services
        })


def status_of_user(request):
    if request.method == "POST":
        status_of_users_name = request.POST["name"]
        status_of_users = StatusOfUsers(status_of_users_name = status_of_users_name)
        status_of_users.save()
        return render(request, 'feed/status_of_user.html', {})
    else:
        return render(request, 'feed/status_of_user.html', {})


def new_user(request):
    all_levels = Level.objects.all()
    all_status = StatusOfUsers.objects.all()
    if request.method == "POST":
        level_reference = request.POST["lev"]
        level_reference = int(level_reference)
        status_of_users_reference = request.POST["st"]
        status_of_users_reference = int(status_of_users_reference)
        name = request.POST["name"]
        passwd = request.POST["passwd"]
        email = request.POST["email"]
        new_user = User(level_name = Level(level_reference), status_of_users_name = StatusOfUsers(status_of_users_reference) ,name = name, passwd = passwd,email = email)
        new_user.save()
    else:    
        return render(request, 'feed/new_user.html', {
            "levels" : all_levels,
            "status" : all_status
         })
    return render(request, 'feed/new_user.html', {
            "levels" : all_levels,
            "status" : all_status


         })


def clients(request):
    all_clients = Client.objects.all()
    return render(request, 'feed/clients.html', {
        "all" : all_clients
        })


def users(request):
    all_users = User.objects.all()
    return render(request, 'feed/users.html', {
        "allusers" : all_users,
        })


def new_client(request):
    if request.method == "POST":
        name = request.POST["name"]
        company = request.POST["company"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        adress = request.POST["adress"]
        if Client.objects.filter(email = email).exists():
            messages.success(request, ("el email ya existe"))
            return redirect ('new_client')
        new_client = Client(name = name, company_name = company, email = email, phonenumber = phone, adress = adress)
        new_client.save()
        messages.success(request, ("Cliente creado"))
        return render(request, 'feed/new_client.html', {})
    else:
        return render(request, 'feed/new_client.html', {})


def items(request):
    all_items = Item.objects.all()
    return render(request, 'feed/items.html', {
        "all_items" : all_items
    })


def new_item(request):
    all_types_of_items = TypeOfItem.objects.all()
    if request.method == "POST":
        type_of_item = request.POST["type"]
        type_of_item = int(type_of_item)
        model = request.POST["model"]
        brand = request.POST["brand"]
        if Item.objects.filter(model = model).exists():
            messages.success(request, ("El item ya existe"))
            return redirect ('new_item')
        new_item = Item(type_of_item = TypeOfItem(type_of_item), model = model, brand = brand)
        new_item.save()
        return render(request, 'feed/new_item.html', {
            "all_types_of_items" : all_types_of_items
        })
    else:
        return render(request, 'feed/new_item.html', {
            "all_types_of_items" : all_types_of_items
        })


def new_type_of_item(request):
    if request.method == "POST":
        type_of_item = request.POST["type_of_item"]
        if TypeOfItem.objects.filter(description = type_of_item).exists():
            messages.success(request, ("El item ya existe"))
            return redirect ('new_type_of_item')
        new_type_of_item = TypeOfItem(description = type_of_item)
        new_type_of_item.save()
        return render(request, 'feed/new_type_of_item.html', {})
    else:
        return render(request, 'feed/new_type_of_item.html', {})



def levels(request):
    all_levels = Level.objects.all()
    return render(request, 'feed/levels.html', {
        "all_levels" : all_levels
    })


def new_level(request):
    if request.method == "POST":
        level_name = request.POST["name"]
        description = request.POST["description"]
        reference_number = request.POST["number"]
        new_level = Level(level_name = level_name, description = description)
        new_level.save()
        return render(request, 'feed/new_level.html', {})
    else:
        return render(request, 'feed/new_level.html', {})


def user_status(request):
    all_status = StatusOfUsers.objects.all()
    return render(request, 'feed/user_status.html', {
        "all_status" : all_status
    })


def service_status(request):
    all_status = Status.objects.all()
    return render(request, 'feed/service_status.html', {
        "all_status" : all_status
    })


def new_service_status(request):
    if request.method == "POST":
        name = request.POST["name"]
        new_service_status = Status(name = name)
        new_service_status.save()
        return render(request, 'feed/new_service_status.html', {})
    else:
        return render(request, 'feed/new_service_status.html', {})


def user_detail(request, user_id):
    user = User.objects.get(pk = user_id)
    all_user_services = Service.objects.filter(user_id = user)
    return render(request, 'feed/user_detail.html', {
        "user" : user,
        "all_user_services": all_user_services
    })


def new_service(request):
    if request.user.is_superuser:
        all_users = User.objects.all()
    else:      
        user_id = request.user.id
        all_users = User.objects.filter(id = user_id)   
    all_service_types = TypeOfService.objects.all()
    all_product_types = TypeOfProduct.objects.all()
    all_clients = Client.objects.all()
    all_status = Status.objects.all()
    if request.method == "POST":
        user_reference = request.POST["user"]
        user_reference = int(user_reference)
        service_reference = request.POST["service"]
        service_reference = int(service_reference)
        product_reference = request.POST["product"]
        product_reference = int(product_reference)
        client_reference = request.POST["client"]
        client_reference = int(client_reference)
        model = request.POST["model"]
        serial_number = request.POST["serial"]
        accesories = request.POST["acce"]
        failure = request.POST["failure"]
        is_working = request.POST.get('working')
        if is_working:
            is_working = True
        else:
            is_working = False
        print(is_working)
        is_damaged = request.POST.get('damaged')
        if is_damaged:
            is_damaged = True
        else:
            is_damaged = False
        print(is_damaged)
        is_complete = request.POST.get('complete')
        if is_complete:
            is_complete = True
        else:
            is_complete = False
        print(is_complete)
        service_price = request.POST["price"]
        #client_pass= request.POST["reference"]
        existe = False
        while existe == False:
            client_pass = get_random_string(length = 10)
            if Service.objects.filter(client_pass = client_pass).exists():
                existe = False
            else:
                existe = True
        new_service = Service(user = User(user_reference), service_type = TypeOfService(service_reference), type_of_product = TypeOfProduct(product_reference), client = Client(client_reference), status = Status(1), model = model, serial_number = serial_number, accesories = accesories, failure = failure, is_working = is_working, is_damaged = is_damaged, is_complete = is_complete, service_price = service_price, client_pass = client_pass)
        new_service.save()
        messages.success(request, ("Servicio creado"))
        return render(request, 'feed/new_service.html', {
            "users" : all_users,
            "services" : all_service_types,
            "products" : all_product_types,
            "clients" : all_clients,
            "status" : all_status
         })
    else:    
        return render(request, 'feed/new_service.html', {
            "users" : all_users,
            "services" : all_service_types,
            "products" : all_product_types,
            "clients" : all_clients,
            "status" : all_status,
         })


def service_detail(request, service_id):
    all_item_details = ItemDetail.objects.filter(service = service_id)
    all_items = Item.objects.all()
    price = 0
    for item in all_item_details:
        price = price + item.price
    service = Service.objects.get(pk = service_id)
    price = price + service.service_price
    price = float(price)
    price = int(round(price, 0))
    all_service_comments = ServiceComment.objects.filter(service = service_id)
    if service.is_working:
        working_si_no = "Si"
    else:
        working_si_no = "No"
    if service.is_damaged:
        damaged_si_no = "Si"
    else:
        damaged_si_no = "No"
    if service.is_complete:
        complete_si_no = "Si"
    else:
        complete_si_no = "No"
    if request.method == "POST" and request.POST.get("form_type") == 'form_item':
        item_id = request.POST["id"]
        item_id = int(item_id)
        type_of_item = request.POST["item"]
        type_of_item = int(type_of_item)
        serial = request.POST["serial_number"]
        reference = request.POST["reference"]
        price = request.POST["price"]
        new_item = ItemDetail(service = Service(item_id),item = Item(type_of_item), serial_number = serial, reference = reference, price = price)
        new_item.save()
        return render(request, 'feed/service_detail.html', {
        "all_item_details": all_item_details,
        "service": service,
        "items": all_items,
        "working_si_no": working_si_no,
        "damaged_si_no": damaged_si_no,
        "complete_si_no": complete_si_no
        })
    if request.method == "POST" and request.POST.get("form_type") == 'form_comment':
        comment_id = request.POST["service_id_comment"]
        comment_id = int(comment_id)
        comment_comment = request.POST["comment"]
        new_service_comment = ServiceComment( service = Service(comment_id) , comment = comment_comment)
        new_service_comment.save()
    return render(request, 'feed/service_detail.html', {
        "all_item_details": all_item_details,
        "all_service_comments": all_service_comments,
        "service": service,
        "items": all_items,
        "working_si_no": working_si_no,
        "damaged_si_no": damaged_si_no,
        "complete_si_no": complete_si_no,
        "price": price
    })


def client_detail(request, client_id):
    client = Client.objects.get(pk = client_id)
    all_client_services = Service.objects.filter(client_id = client)
    return render(request, 'feed/client_detail.html', {
        "client" : client,
        "all_client_services": all_client_services
    })


def home(request):
    if request.user.is_superuser:
        all_services = Service.objects.all().order_by('-created')
        counter = all_services.count()
        unfinished_services = Service.objects.filter(
        Q(status__lt = 5) |
        Q(status__gt = 5)
        )
        finished_services = Service.objects.filter(status = 5)
    else:      
        user_id = request.user.id
        all_services = Service.objects.filter(user = user_id).order_by('-created')
        counter = all_services.count()
        unfinished_services = Service.objects.filter(
            Q(status__lt = 5) |
            Q(status__gt = 5),
            user = user_id
        )
        finished_services = Service.objects.filter(
            user = user_id,
            status = 5
            )
    unfinished_services = unfinished_services.count()
    finished_services = finished_services.count()
    return render(request, 'feed/home.html', {
        "all" : all_services,
        "counter": counter,
        "unfinished_services": unfinished_services,
        "finished_services": finished_services
        })


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("BIENVENIDO    " + username))
            return redirect ('/home/')
        else:
            messages.success(request, ("Correo o usuario incorrecto"))
            return render(request, 'feed/services.html', {}) 
    else:
        return render(request, 'feed/home.html', {})


def update_service(request, service_id):
    all_service_types = TypeOfService.objects.all()
    all_service_status = Status.objects.all()
    all_item_details = ItemDetail.objects.filter(service = service_id)
    all_items = Item.objects.all()
    price = 0
    for item in all_item_details:
        price = price + item.price
    service = Service.objects.get(pk = service_id)
    current_model = service.model
    current_serial_number = service.serial_number
    current_price = service.service_price
    current_status = service.status.name
    current_status_id = service.status.id
    price = price + service.service_price
    all_service_comments = ServiceComment.objects.filter(service = service_id)
    if service.is_working:
        working_si_no = "Si"
    else:
        working_si_no = "No"
    if service.is_damaged:
        damaged_si_no = "Si"
    else:
        damaged_si_no = "No"
    if service.is_complete:
        complete_si_no = "Si"
    else:
        complete_si_no = "No"
    if request.method == "POST" and request.POST.get("form_type") == 'form_service':
        saved_count = 0
        #service_reference = request.POST["stat"]
        #service_reference = int(service_reference)
        status_reference = request.POST.get("stat")
        if status_reference:
            status_reference = int(status_reference)
            status_updated = Service.objects.get(pk = service_id)
            status_updated.status = Status(status_reference)
            status_updated.save()
            saved_count = saved_count + 1    
        model = request.POST["model"]
        if not model:
            model = current_model        
        else:
            model_updated = Service.objects.get(pk = service_id)
            model_updated.model = model
            model_updated.save()
            saved_count = saved_count + 1                    
        serial_number = request.POST["serial"]
        if not serial_number:
            serial_number = current_serial_number
        else:
            serial_updated = Service.objects.get(pk = service_id)
            serial_updated.serial_number = serial_number
            serial_updated.save()
            saved_count = saved_count + 1
        service_price = request.POST["price"]
        if not service_price:
            service_price = float(current_price)
        else:
            service_price = int(service_price)
            price_updated = Service.objects.get(pk = service_id)
            price_updated.service_price = service_price
            price_updated.save()
            saved_count = saved_count + 1
        if saved_count > 0:  
            messages.success(request, ("usuario actualizado"))
            return redirect ('update_service', service_id)
        else:
            messages.success(request, ("no modificaste datos"))
    if request.method == "POST" and request.POST.get("form_type") == 'form_item_update':
        item_id = request.POST["id"]
        item_id = int(item_id)
        type_of_item = request.POST["item"]
        type_of_item = int(type_of_item)
        serial = request.POST["serial_number"]
        if ItemDetail.objects.filter(serial_number = serial).exists():
            messages.success(request, ("el numero de serie del item ya existe"))
            return redirect ('update_service', service_id)
        reference = request.POST["reference"]
        price = request.POST["price"]
        new_item = ItemDetail(service = Service(item_id),item = Item(type_of_item), serial_number = serial, reference = reference, price = price)
        new_item.save()
        messages.success(request, ("item agregado"))
        return redirect ('update_service', service_id)
    if request.method == "POST" and request.POST.get("form_type") == 'form_comment_update':
        comment_id = request.POST["service_id_comment"]
        comment_id = int(comment_id)
        comment_comment = request.POST["comment"]
        new_service_comment = ServiceComment( service = Service(comment_id) , comment = comment_comment)
        new_service_comment.save()
        return redirect ('update_service', service_id)
        #return render(request, 'feed/update_service.html', {
        #"all_item_details": all_item_details,
        #"service": service,
        #"items": all_items,
        #})
        #update_service = Service(user = User(service.user.id), service_type = TypeOfService(service.service_type.id), type_of_product = TypeOfProduct(service.type_of_product.id), client = Client(service.client.id), status = Status(status_reference), model = model, serial_number = serial_number, is_working = service.is_working , is_damaged = service.is_damaged, is_complete = service.is_complete, service_price = service_price)
        #update_service.update(service = service_id)
        #return HttpResponse("status_reference")
        #return render(request, 'feed/update_service.html', {
        #"all_item_details": all_item_details,
        #"services_types" : all_service_types,
        #"service": service,
        #"items": all_items,
        #"working_si_no": working_si_no,
        #"damaged_si_no": damaged_si_no,
        #"complete_si_no": complete_si_no,
        #"status": all_service_status,
        #"current_status": current_status
        #})
    #formulario de items   
    return render(request, 'feed/update_service.html', {
        "all_item_details": all_item_details,
        "services_types" : all_service_types,
        "all_service_comments": all_service_comments,
        "service": service,
        "items": all_items,
        "working_si_no": working_si_no,
        "damaged_si_no": damaged_si_no,
        "complete_si_no": complete_si_no,
        "price": price,
        "status": all_service_status,
        "current_status": current_status,
        "current_status_id": current_status_id
    })


def update_client(request, client_id):
    saved_count = 0
    client = Client.objects.get(pk = client_id)
    all_client_services = Service.objects.filter(client_id = client)
    if request.method == "POST":
        company_name = request.POST["company_name"]
        if company_name:
            company_name_updated = Client.objects.get(pk = client_id)
            company_name_updated.company_name = company_name
            company_name_updated.save()
            saved_count = saved_count + 1      
        email = request.POST["email"]
        if email:
            email_updated = Client.objects.get(pk = client_id)
            email_updated.email = email
            email_updated.save()
            saved_count = saved_count + 1             
        name = request.POST["name"]
        if name:
            name_updated = Client.objects.get(pk = client_id)
            name_updated.name = name
            name_updated.save()
            saved_count = saved_count + 1              
        phonenumber = request.POST["phonenumber"]
        if phonenumber:
            phonenumber_updated = Client.objects.get(pk = client_id)
            phonenumber_updated.phonenumber = phonenumber
            phonenumber_updated.save()
            saved_count = saved_count + 1             
        adress = request.POST["adress"]
        if adress:
            adress_updated = Client.objects.get(pk = client_id)
            adress_updated.adress = adress
            adress_updated.save()
            saved_count = saved_count + 1            
        if saved_count > 0:  
            messages.success(request, ("cliente actualizado"))
            return redirect ('update_client', client_id)
        else:
            messages.success(request, ("no modificaste datos"))
    return render(request, 'feed/update_client.html', {
        "client" : client,
        "all_client_services": all_client_services
    })


def client_view(request):
    if request.method == "POST":
        client_code = request.POST["code"]
        if Service.objects.filter( client_pass = client_code).exists():
            client_code = Service.objects.get(client_pass = client_code)
            client_id = client_code.id
            messages.success(request, ("bienvenido"))
            return redirect ('client_view_detail', client_id)
        else:
            messages.success(request, ("Clave incorecta"))
            return redirect ('client_view')
    return render(request, 'feed/client_view.html', {
    })


def client_view_detail(request, client_id):
    client_service = Service.objects.get( pk = client_id)
    all_service_comments = ServiceComment.objects.filter(service = client_service.id)
    all_item_details = ItemDetail.objects.filter(service = client_service.id)
    all_items = Item.objects.all()
    #tiempo = datetime.datetime.strftime(exact_moment,"%m")
    tiempo = datetime.datetime.now()
    if client_service.is_working:
        working_si_no = "Si"
    else:
        working_si_no = "No"
    if client_service.is_damaged:
        damaged_si_no = "Si"
    else:
        damaged_si_no = "No"
    if client_service.is_complete:
        complete_si_no = "Si"
    else:
        complete_si_no = "No"
    price = 0
    for item in all_item_details:
        price = price + item.price
    service = Service.objects.get(pk = client_service.id)
    price = price + service.service_price
    price = float(price)
    price = int(round(price, 2))
    return render (request, 'feed/client_view_detail.html',{
        "tiempo": tiempo,
        "client_id": client_id,
        "client_service": client_service,
        "working_si_no": working_si_no,
        "damaged_si_no": damaged_si_no,
        "complete_si_no": complete_si_no,
        "all_service_comments": all_service_comments,
        "all_item_details": all_item_details,
        "price": price
        #"service": service,
        #"items": all_items,
    })

       

def reports(request):
    full_prices = []
    full_prices_iva = []
    iva_price = 0
    total_price = 0
    total_price_iva = 0
    service_item_price = 0
    service_item_price_iva = 0
    just_service_price = 0
    just_service_price_iva = 0
    comisions = 0
    all_status = Status.objects.all()
    if request.user.is_superuser:
        #all_item_details = ItemDetail.objects.filter(service = service_id)
        all_services = Service.objects.all()
        all_users = User.objects.all()
    else:      
        user_id = request.user.id
        all_services = Service.objects.filter(user = user_id)
        all_users = User.objects.filter(id = user_id)   
    for serv in all_services:
        items = ItemDetail.objects.filter(service = serv.id)
        service_full_price = 0
        just_service_price = just_service_price + serv.service_price
        for item in items:
            service_full_price = service_full_price + item.price
            service_item_price = service_item_price + item.price
        service_full_price = service_full_price + serv.service_price
        full_prices.append(service_full_price)
    service_item_price_iva = round(float(service_item_price) /1.16,2)
    for full in full_prices:
        total_price = round(float(total_price) + float(full),2)
    total_price_iva = float(total_price_iva)
    total_price_iva = round(total_price / 1.16, 2)
    just_service_price_iva = float(just_service_price_iva)
    just_service_price_iva = round(float(just_service_price) / 1.16,2)
    comisions = round(just_service_price_iva *.30,2)
    number_of_services = all_services.count()
    if request.method == "POST" and request.POST.get("form_type") == 'form_month':
        total_price = 0
        total_price_iva = 0
        full_prices = []
        service_item_price = 0
        service_item_price_iva = 0
        just_service_price = 0
        just_service_price_iva = 0
        comisions = 0
        mes = request.POST.get('month')
        if mes == 0 or mes =="0" :
            messages.success(request, (" Te falto llenar un campo"))
            return redirect('reports')
        list_services = Service.objects.filter( 
            created__month = mes
        )
        for serv in list_services:
            items = ItemDetail.objects.filter(service = serv.id)
            service_full_price = 0
            just_service_price = just_service_price + serv.service_price
            for item in items:
                service_full_price = service_full_price + item.price
                service_item_price = service_item_price + item.price
            service_full_price = service_full_price + serv.service_price
            full_prices.append(service_full_price)  
        service_item_price_iva = round(float(service_item_price) /1.16,2)
        for full in full_prices:
            total_price = round(float(total_price) + float(full),2)
        total_price_iva = float(total_price_iva)
        total_price_iva = round(total_price / 1.16, 2)
        just_service_price_iva = float(just_service_price_iva)
        just_service_price_iva = round(float(just_service_price) / 1.16,2)
        number_of_services = list_services.count()  
        comisions = round(just_service_price_iva *.30,2)
        return render(request, 'feed/reports.html', {
        "all" : list_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })
    if request.method == "POST" and request.POST.get("form_type") == 'form_user_month':
        full_prices = []
        full_prices_iva = []
        total_price = 0
        total_price_iva = 0
        service_item_price = 0
        service_item_price_iva = 0
        just_service_price = 0
        just_service_price_iva = 0
        comisions = 0
        mes = request.POST.get('month')
        selected_user = request.POST["selected_user"]
        list_services = Service.objects.filter( 
            created__month = mes,
            user = selected_user
        )
        number_of_services = list_services.count() 
        if mes == 0 or mes == "0" or selected_user == 0 or selected_user == "0":
            messages.success(request, (" Te falto llenar un campo"))
            return render(request, 'feed/reports.html', {
            "all" : list_services,
            "all_users": all_users,
            "full_prices": full_prices,
            "full_prices_iva": full_prices_iva,
            "all_status": all_status,
        })
        for serv in list_services:
            items = ItemDetail.objects.filter(service = serv.id)
            service_full_price = 0
            just_service_price = just_service_price + serv.service_price
            for item in items:
                service_full_price = service_full_price + item.price
                service_item_price = service_item_price + item.price
            service_full_price = service_full_price + serv.service_price
            full_prices.append(service_full_price)  
            full_prices_iva.append(iva_price)
        service_item_price_iva = round(float(service_item_price) /1.16,2)
        for full in full_prices:
            total_price = round(float(total_price) + float(full),2)
        total_price_iva = float(total_price_iva)
        total_price_iva = round(total_price / 1.16, 2)
        just_service_price_iva = float(just_service_price_iva)
        just_service_price_iva = round(float(just_service_price) / 1.16,2)
        comisions = round(just_service_price_iva *.30,2)
        return render(request, 'feed/reports.html', {
        "all" : list_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "full_prices_iva": full_prices_iva,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })        
    if request.method == "POST" and request.POST.get("form_type") == 'form_user':
        full_prices = []
        full_prices_iva = []
        total_price = 0
        total_price_iva = 0
        service_item_price = 0
        service_item_price_iva = 0
        just_service_price = 0
        just_service_price_iva = 0
        comisions = 0
        selected_user = request.POST["selected_user"]
        list_services = Service.objects.filter( 
            user = selected_user
        )
        number_of_services = list_services.count() 
        if selected_user == 0 or selected_user == "0":
            messages.success(request, (" Te falto llenar un campo"))
            return render(request, 'feed/reports.html', {
            "all" : list_services,
            "all_users": all_users,
            "full_prices": full_prices,
            "full_prices_iva": full_prices_iva,
            "all_status": all_status,
        })
        for serv in list_services:
            items = ItemDetail.objects.filter(service = serv.id)
            service_full_price = 0
            just_service_price = just_service_price + serv.service_price
            for item in items:
                service_full_price = service_full_price + item.price
                service_item_price = service_item_price + item.price
            service_full_price = service_full_price + serv.service_price
            full_prices.append(service_full_price)
            full_prices_iva.append(iva_price)
        service_item_price_iva = round(float(service_item_price) /1.16,2)
        for full in full_prices:
            total_price = round(float(total_price) + float(full),2)
        total_price_iva = float(total_price_iva)
        total_price_iva = round(total_price / 1.16, 2)
        just_service_price_iva = float(just_service_price_iva)
        just_service_price_iva = round(float(just_service_price) / 1.16,2)
        comisions = round(just_service_price_iva *.30,2)
        return render(request, 'feed/reports.html', {
        "all" : list_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "full_prices_iva": full_prices_iva,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })
    if request.method == "POST" and request.POST.get("form_type") == 'form_status':
        full_prices = []
        full_prices_iva = []
        total_price = 0
        total_price_iva = 0
        service_item_price = 0
        service_item_price_iva = 0
        just_service_price = 0
        just_service_price_iva = 0
        comisions = 0
        selected_status = request.POST["selected_status"]
        list_services = Service.objects.filter( 
            status = selected_status
        )
        number_of_services = list_services.count() 
        if selected_status == 0 or selected_status == "0":
            messages.success(request, (" Te falto llenar un campo"))
            return render(request, 'feed/reports.html', {
            "all" : list_services,
            "all_users": all_users,
            "full_prices": full_prices,
            "full_prices_iva": full_prices_iva,
            "all_status": all_status,
        })
        for serv in list_services:
            items = ItemDetail.objects.filter(service = serv.id)
            service_full_price = 0
            just_service_price = just_service_price + serv.service_price
            for item in items:
                service_full_price = service_full_price + item.price
                service_item_price = service_item_price + item.price
            service_full_price = service_full_price + serv.service_price
            full_prices.append(service_full_price)
            full_prices_iva.append(iva_price)
        service_item_price_iva = round(float(service_item_price) /1.16,2)
        for full in full_prices:
            total_price = round(float(total_price) + float(full),2)
        total_price_iva = float(total_price_iva)
        total_price_iva = round(total_price / 1.16, 2)
        just_service_price_iva = float(just_service_price_iva)
        just_service_price_iva = round(float(just_service_price) / 1.16,2)
        comisions = round(just_service_price_iva *.30,2)
        return render(request, 'feed/reports.html', {
        "all" : list_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "full_prices_iva": full_prices_iva,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })
    if request.method == "POST" and request.POST.get("form_type") == 'form_date':
        full_prices = []
        full_prices_iva = []
        total_price = 0
        total_price_iva = 0
        service_item_price = 0
        service_item_price_iva = 0
        just_service_price = 0
        just_service_price_iva = 0
        comisions = 0
        specific_date = request.POST.get("specific_date")
        selected_user = request.POST["selected_user"]
        selected_status = request.POST["selected_status"]
        if specific_date == None or specific_date == '':
            messages.success(request, (" debes elejir una fecha"))
            return render(request, 'feed/reports.html', {
            "all_users": all_users,
            "full_prices": full_prices,
            "full_prices_iva": full_prices_iva,
            "all_status": all_status,
        })
        if specific_date and selected_user != "no selection" and selected_status != "no selection":
            search_date = datetime.datetime.fromisoformat(specific_date)
            list_services = Service.objects.filter( 
                user = selected_user,
                created__year = search_date.year,
                created__month = search_date.month,
                created__day = search_date.day, 
                status = selected_status
            )
        elif specific_date and selected_user != "no selection" :
            search_date = datetime.datetime.fromisoformat(specific_date)
            list_services = Service.objects.filter( 
                user = selected_user,
                created__year = search_date.year,
                created__month = search_date.month,
                created__day = search_date.day
            )
        elif specific_date and selected_status != "no selection" :
            search_date = datetime.datetime.fromisoformat(specific_date)
            list_services = Service.objects.filter( 
                created__year = search_date.year,
                created__month = search_date.month,
                created__day = search_date.day,
                status = selected_status
            )
        elif specific_date:
            search_date = datetime.datetime.fromisoformat(specific_date)
            list_services = Service.objects.filter( 
                created__year = search_date.year,
                created__month = search_date.month,
                created__day = search_date.day
            )
        number_of_services = list_services.count() 
        for serv in list_services:
            items = ItemDetail.objects.filter(service = serv.id)
            service_full_price = 0
            just_service_price = just_service_price + serv.service_price
            for item in items:
                service_full_price = service_full_price + item.price
                service_item_price = service_item_price + item.price
            service_full_price = service_full_price + serv.service_price
            full_prices.append(service_full_price)
            full_prices_iva.append(iva_price)
        for full in full_prices:
            total_price = round(float(total_price) + float(full),2)
        total_price_iva = float(total_price_iva)
        total_price_iva = round(total_price / 1.16, 2)
        just_service_price_iva = float(just_service_price_iva)
        just_service_price_iva = round(float(just_service_price) / 1.16,2)
        comisions = round(just_service_price_iva *.30,2)
        return render(request, 'feed/reports.html', {
        "all" : list_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "full_prices_iva": full_prices_iva,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })      
    if request.method == "POST" and request.POST.get("form_type") == 'form_date_range':
        full_prices = []
        full_prices_iva = []
        total_price = 0
        total_price_iva = 0
        service_item_price = 0
        service_item_price_iva = 0
        just_service_price = 0
        just_service_price_iva = 0
        comisions = 0
        initial_date = request.POST.get("initial_date")
        final_date = request.POST.get("final_date")
        selected_user = request.POST["selected_user"]
        selected_status = request.POST["selected_status"]
        if initial_date == '' or initial_date == None or final_date == '' or final_date == None:
            messages.success(request, (" Te falto llenar un campo"))
            return render(request, 'feed/reports.html', {
            #"all" : list_services,
            "all_users": all_users,
            "full_prices": full_prices,
            "full_prices_iva": full_prices_iva,
            "all_status": all_status
        })
        search_initial_date = datetime.datetime.fromisoformat(initial_date)
        search_final_date = datetime.datetime.fromisoformat(final_date)
        if initial_date >= final_date:
            messages.success(request, (" la fecha inicial no puede ser mayor o igual a la fecha final "))
            return render(request, 'feed/reports.html', {
            #"all" : list_services,
            "all_users": all_users,
            "full_prices": full_prices,
            "full_prices_iva": full_prices_iva,
            "all_status": all_status,
        })
        if initial_date and final_date and selected_user != "no selection" and selected_status != "no selection":
            search_initial_date = datetime.datetime.fromisoformat(initial_date)
            search_final_date = datetime.datetime.fromisoformat(final_date)
            list_services = Service.objects.filter( 
                created__gte = search_initial_date,
                created__lte = search_final_date + datetime.timedelta(days=1),
                user = selected_user,
                status = selected_status
            ) 
        elif initial_date and final_date and selected_user != "no selection":
            search_initial_date = datetime.datetime.fromisoformat(initial_date)
            search_final_date = datetime.datetime.fromisoformat(final_date)
            list_services = Service.objects.filter( 
                created__gte = search_initial_date,
                created__lte = search_final_date + datetime.timedelta(days=1),
                user = selected_user
            ) 
        elif initial_date and final_date and selected_status != "no selection":
            search_initial_date = datetime.datetime.fromisoformat(initial_date)
            search_final_date = datetime.datetime.fromisoformat(final_date)
            list_services = Service.objects.filter( 
                created__gte = search_initial_date,
                created__lte = search_final_date + datetime.timedelta(days=1),
                status = selected_status
            )
        elif initial_date and final_date:
            search_initial_date = datetime.datetime.fromisoformat(initial_date)
            search_final_date = datetime.datetime.fromisoformat(final_date)
            list_services = Service.objects.filter( 
                created__gte = search_initial_date,
                created__lte = search_final_date + datetime.timedelta(days=1)
            )  
        number_of_services = list_services.count()
        
        for serv in list_services:
            items = ItemDetail.objects.filter(service = serv.id)
            service_full_price = 0
            just_service_price = just_service_price + serv.service_price
            for item in items:
                service_full_price = service_full_price + item.price
                service_item_price = service_item_price + item.price
            service_full_price = service_full_price + serv.service_price
            full_prices.append(service_full_price)
            full_prices_iva.append(iva_price)
        for full in full_prices:
            total_price = round(float(total_price) + float(full),2)
        total_price_iva = float(total_price_iva)
        total_price_iva = round(total_price / 1.16, 2)
        just_service_price_iva = float(just_service_price_iva)
        just_service_price_iva = round(float(just_service_price) / 1.16,2)
        comisions = round(just_service_price_iva *.30,2)
        return render(request, 'feed/reports.html', {
        "all" : list_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "full_prices_iva": full_prices_iva,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })    

    return render(request, 'feed/reports.html', {
        "all" : all_services,
        "all_users": all_users,
        "full_prices": full_prices,
        "full_prices_iva": full_prices_iva,
        "all_status": all_status,
        "number_of_services": number_of_services,
        "total_price": total_price,
        "total_price_iva": total_price_iva,
        "service_item_price": service_item_price,
        "service_item_price_iva": service_item_price_iva,
        "just_service_price": just_service_price,
        "just_service_price_iva": just_service_price_iva,
        "comisions": comisions
        })