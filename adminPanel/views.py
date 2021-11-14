from json.decoder import JSONDecodeError
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.views.decorators import csrf
from .models import Order, Product, User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers



prod = Product.objects.all()

def getData(body):
    response_json = json.dumps(body)
    data = json.loads(response_json)
    return data




def homePage(request):
    return render(request, 'Main.html', {"prods": prod})


def displayProduct(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'Details.html', {"prod": product})


def adminPanel(request):
    return render(request, 'Admin.html',  {"prods": prod})


@csrf_exempt
def adminView(request):
    if request.method == 'POST':
        data = getData(request.POST)
        if data["email"] == "saadahmed_sh":
            if data["lname"] == "123456":
                return JsonResponse({'authenticated': 'true'})
        return JsonResponse({'authenticated': 'false'})


def productsDetail(request):
    return render(request, 'adminView.html')


def returnProductsToAdmin(request):
    return HttpResponse(
        serializers.serialize("json", Product.objects.all()),
        content_type="application/json")


@csrf_exempt
def editProduct(request):
    if request.method == 'POST':
        id = request.POST.get("user_id")
        prod = Product.objects.get(id=id)

        prod.productName = request.POST.get("product_name")
        prod.productPrice = request.POST.get("product_price")
        prod.productLocation = request.POST.get("product_location")
        prod.productTime = request.POST.get("product_time")
        prod.productSpecification = request.POST.get("product_description")
        if request.FILES.get('product_image') is not None:
            prod.imageURL = request.FILES["product_image"]

        prod.save()
        return render(request, 'adminView.html')


@csrf_exempt
def addProduct(request):
    try:
        prod = Product()
        prod.productName = request.POST.get("product_name")
        prod.productPrice = request.POST.get("product_price")
        prod.productLocation = request.POST.get("product_location")
        prod.productTime = request.POST.get("product_time")
        prod.productSpecification = request.POST.get("product_description")
        prod.imageURL = request.FILES["product_image"]
        prod.save()
    except:
         return render(request, 'adminView.html')
    return render(request, 'adminView.html')

    



def registerUser(request):
    return render(request, 'Register.html')


@csrf_exempt
def addUser(request):
    if request.method == 'POST':
        model_data = serializers.serialize("json", User.objects.all())
        data = getData(request.POST)
        model_data = json.loads(model_data)

        if model_data is not None:
            for model in model_data:
                if model["fields"]["email"] == data["email"]:
                    return JsonResponse({"registered": "false"})

        user = User()
        user.full_name = data["fullname"]
        user.email = data["email"]
        user.password = data["password"]
        user.cnic = data["cnic"]
        user.number = data["number"]
        user.status = 0  # unregistered for the time being
        user.save()
        return JsonResponse({'registered': 'true'})


def adminUser(request):
    return render(request, 'Users.html')


def returnUsers(request):

    return HttpResponse(
        serializers.serialize("json", User.objects.all()),
        content_type="application/json")


@csrf_exempt
def editUser(request):
    if request.method == 'POST':
        id = request.POST.get("user_id")
        user = User.objects.get(id=id)
        if user.status == 0:
            user.status = 1
        else:
            user.status = 0

    user.save()

    return JsonResponse({"update": "ok"})


@csrf_exempt
def updateUser(request):
    if request.method == 'POST':
        data = getData(request.POST)
        user = User.objects.get(id=data["id"])
        user.full_name = data["fullname"]
        user.email = data["email"]
        user.password = data["password"]
        user.cnic = data["cnic"]
        user.number = data["number"]
        user.save()
        return JsonResponse({'update': 'true'})


@csrf_exempt
def allowUser(request):
    if request.method == 'POST':
        data = getData(request.POST)
        model_data = serializers.serialize("json", User.objects.all())
        model_data = json.loads(model_data)
        if model_data is not None:
            for model in model_data:
                if model["fields"]["email"] == data["email"]:
                    if model["fields"]["status"] == 0:
                        return JsonResponse({"authorized": "false"})
                    else:
                        return JsonResponse({"authorized": "true",
                                             "id": model["pk"]})
        return JsonResponse({"authorized": "no"})


@csrf_exempt
def addOrder(request):
    if request.method == 'POST':
        data = getData(request.POST)
        model_data = serializers.serialize("json", Order.objects.all())
        model_data = json.loads(model_data)

        if model_data is not None:
            for model in model_data:
                if model["fields"]["user_id"] == int(data["user_id"]) and model["fields"]["product_id"] == int(data["product_id"]):
                    bid = Order.objects.get(user_id=int(
                        data["user_id"]), product_id=int(data["product_id"]))
                    bid.bid_price = data["price"]
                    bid.save()
                    return JsonResponse({"exists": "true"})

        order = Order()
        order.product_id = int(data["product_id"])
        order.user_id = int(data["user_id"])
        order.bid_price = int(data["price"])
        order.status=0 #order still in processing
        order.save()
        return JsonResponse({"exists": "false"})


def checkout(request):
    return render(request, "Checkout.html")


def getWinnerProduct(id):
    model_data = serializers.serialize("json", Order.objects.all())
    model_data = json.loads(model_data)
    models=[]
    for model in model_data:
        if model["fields"]["product_id"] == int(id):
            models.append(model)
    return models



@csrf_exempt
def winner(request):
    if request.method == 'POST':
        data = getData(request.POST)
        model_data=getWinnerProduct(data["product_id"])
        _model = ' '
        price = -1
        if model_data is not None:
            for model in model_data:
        
                if model["fields"]["bid_price"] > price:
                    _model = model
                    price = model["fields"]["bid_price"]
        if _model != ' ':
            winnerUser=Order.objects.get(user_id=_model["fields"]["user_id"],product_id=_model["fields"]["product_id"])
            winnerUser.status=1
            winnerUser.save()
            return JsonResponse({"status": "ok"})
   
        return JsonResponse({"status": "no bids"})
   



            



@csrf_exempt
def checkIfAuthenticated(request):
    if request.method == 'POST':
        data = getData(request.POST)
        user = User.objects.get(id=data["user_id"])
        if user.status == 1:
            return JsonResponse({"allowed": "true"})
        else:
            return JsonResponse({"allowed": "false"})


@csrf_exempt
def returnWinners(request):
    if request.method == 'POST':
        data = getData(request.POST)
        models=Order.objects.all()
        models=serializers.serialize("json",models)
        models=json.loads(models)
        orders=[]
        for model in models:
            if model["fields"]["user_id"] == int(data["user_id"]):
                orders.append(model)
    
      
        return JsonResponse({"data": orders})



   


@csrf_exempt
def returnBidProducts(request):
    if request.method == 'POST':
        data = getData(request.POST)
        productList = data["products"]
        models = []
        for prod in productList:
            if prod != ',':
                models.append(Product.objects.get(id=int(prod)))
        model_data=serializers.serialize("json", models)
        model_data=json.loads(model_data)
        return JsonResponse({"data": model_data}, safe=False)


