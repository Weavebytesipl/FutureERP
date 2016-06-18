from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.serializers import ProductSerializer, NoteSerializer, CategorySerializer

from common.models import Product
from notes.models import Category, Note

# common error dict
err_post = {"error": 1, "message:": "only POST request is supported"}

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def login(request):
    """
    handle login post request and sends back JSON response
    """
    if request.method == 'POST':
        resp = {"error": 1, "message": "invalid username or password"}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            resp["error"] = 0
            resp["user_id"] = user.id
            resp["email"] = user.email
            resp["message"] = "login successfull"
        return JSONResponse(resp, status=400)


@csrf_exempt
def register(request):
    """
    handle register user post request and sends back JSON response
    """
    if not request.method == 'POST':
        return JSONResponse(err_post, status=400)

    resp = {"error": 1, "message": ""}

    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    # checking availability of username
    try:
        if User.objects.get(username=username):
            resp["message"] = "Username already exists !!!"
            return JSONResponse(resp, status=400)
    except:
        pass

    # registering new user
    user = User.objects.create_user(
            username=username,
            password=password,
            email=email
            )
    resp["error"] = 0
    resp["message"] = "Registration successful"
    return JSONResponse(resp, status=400)

@csrf_exempt
def product_list(request):
    """
    List all code products, or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()	
        serializer = ProductSerializer(products, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    functions retrieves, updates or deletes a product.
    """
    try:
        room = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(room)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        room.delete()
        return HttpResponse(status=204)


@csrf_exempt
def category_list(request, user_id):
    """
    List all code categories, or create a new category.
    """
    if request.method == 'GET':
        categories = Category.objects.filter(user=user_id)
        serializer = CategorySerializer(categories, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, user_id, pk):
    """
    functions retrieves, updates or deletes a category.
    """
    try:
        room = Category.objects.get(user=user_id, pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(room)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        room.delete()
        return HttpResponse(status=204)


@csrf_exempt
def note_list(request, user_id):
    """
    List all code notes, or create a new note.
    """
    if request.method == 'GET':
        notes = Note.objects.filter(user=user_id)
        serializer = NoteSerializer(notes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def note_detail(request, user_id, pk):
    """
    functions retrieves, updates or deletes a note.
    """
    try:
        note = Note.objects.get(user=user_id, pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)
