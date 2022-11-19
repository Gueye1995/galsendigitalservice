from ast import Not
from genericpath import exists
from multiprocessing import context
from .models import User
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Post


def index(request):
    return render(request, 'App/index.html')

def about(request):
    return render(request, 'App/pages/about.html')

def contact(request):
    return render(request, 'App/pages/contact.html')

def portfolio(request):
    return render(request, 'App/pages/portfolio.html')

def portfoliodetail(request):
    return render(request, 'App/pages/portoflio-details.html')

def services(request):
    return render(request, 'App/pages/services.html')

def team(request):
    return render(request, 'App/pages/team.html')

def blog(request):

    

    posts = Post.objects.all()
    context = {'posts':posts}

    return render(request, 'App/pages/blog.html', context)

def blogdetails(request, post_id):

    post = Post.objects.get(pk=post_id)
    return render(request, 'App/pages/blog-single.html', {'post':post})

def connexion(request):
    message = ''

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            posts = Post.objects.all()
            return render(request, 'App/pages/blog.html', {'posts':posts})
        else:
            message = 'Identifiants Invalides'
            return render(request, 'App/pages/login.html', {'message':message})
    else:
        return render(request, 'App/pages/login.html')


#inscription
def signup(request):

    message = ""

    if request.method == 'POST':

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is exists:
            message = "Ce nom d'utilisateur est déjà pris"
            return render(request, 'App/pages/signup.html', {'message':message})
        else:
            if request.POST['password'] == request.POST['password2']:     
                username = request.POST['username']
                password = request.POST['password']
                nom = request.POST['lastname']
                prenom = request.POST['firstname']
                email = request.POST['email']

                User.objects.create_user(username=username, email=email, password=password, first_name=prenom, last_name=nom)

                user = authenticate(request, username=username, password=password)
                login(request, user)

                message = f'Bonjour, {user.username}! Vous etes connecte.'
                return render(request, 'App/pages/blog.html', {'message':message})
            else:
                message = "Les deux mots de passe ne correspondent pas."
                return render(request, 'App/pages/signup.html', {'message':message})
    else:
         return render(request, 'App/pages/signup.html', {'message':message})



def deconnexion(request):
    logout(request)
    return render(request, 'App/index.html')


@login_required
def post(request):

    if request.method == "POST":

        message = "Article publié avec succés"
        title = request.POST['title']
        description = request.POST['desc']
        publisher = request.user.id
        print(publisher, "wesh")

        post = Post(title=title, description=description, publisher_id=publisher)
        post.save()
        return render(request, 'App/pages/new_pub.html', {'message':message})

    else:
        return render(request, 'App/pages/new_pub.html')


