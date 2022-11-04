from django.shortcuts import render, HttpResponse
import openai
from django.contrib import messages
from .models import Contact, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

api_keyy = ("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")
# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'index.html')

def blogwriter(request):
    

    
    topic = request.POST.get('topic')
    title = request.POST.get('title')
    keyword = request.POST.get('keyword')
       
        
    api_data = api_keyy
    openai.api_key = api_data


    completion = openai.Completion()

    
    prompt = (f"Generate adequate blog  for the provided blog topic, title and keyword  title {title}  topic {topic} keyword {keyword}")
    response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
    answer = response.choices[0].text.strip()

        
        
    context = {"ans": answer}
    return render(request, 'blogwriter.html', context)

def productdescwriter(request):
    

    
    name = request.POST.get('name')
    title = request.POST.get('title')
    keyword = request.POST.get('keyword')
       
        
    api_data = api_keyy
    openai.api_key = api_data


    completion = openai.Completion()

    
    prompt = (f"Generate product description for the provided product name, title and keyword  title {title}  product name {name} keyword {keyword}")
    response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
    answer = response.choices[0].text.strip()

        
        
    context = {"ans": answer}
    return render(request, 'productdescwriter.html', context)

def namegenerator(request):
    

    
    
    keyword = request.POST.get('keyword')
       
        
    api_data = api_keyy
    openai.api_key = api_data


    completion = openai.Completion()

    
    prompt = (f"Generate business name for the provided keyword {keyword}")
    response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
    answer = response.choices[0].text.strip()

        
        
    context = {"ans": answer}
    return render(request, 'namegenerator.html', context)

def blogideagenerator(request):
    

    
    
    keyword = request.POST.get('keyword')
       
        
    api_data = api_keyy
    openai.api_key = api_data


    completion = openai.Completion()

    
    prompt = (f"Generate a blog idea for the provided keyword {keyword}")
    response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
    answer = response.choices[0].text.strip()

        
        
    context = {"ans": answer}
    return render(request, 'blogidea.html', context)


def contact(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
    return render(request, 'contact.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

   
        user = authenticate(request, email=email, password=password)
        
        if user is not None:

            auth.login(request, user)
            return redirect("index")

    else:
        messages.info(request,  "Invalid Info")
        return render(request, "login.html")
    return render(request, 'login.html')

def createaccount(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email exists")

        
        else:

            
            user = User.objects.create_user(first_name=firstname,last_name=lastname, email=email, password= password)

            user.save()
            messages.info(request, "Registered Successfully")
            return redirect('profile/')
   



    return render(request, 'createaccount.html')

@login_required
def logout(request):
    logout(request)
    return  HttpResponseRedirect('/')

def items(request):
    return render(request, "items.html")
@login_required()
def profile(request):
    image = request.POST.get('image')
    bio = request.POST.get('bio')
    images = Profile(avatar=image)
    images.save
    context = {"bio": bio}
    return render(request, "profile.html")