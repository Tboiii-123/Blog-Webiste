from django.shortcuts import render
#For decorators
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout


from .models import BlogPost


# @login_required(login_url='signin')

def index(request):

    post =BlogPost.objects.all()

    return render(request,'index.html',{

        'posts':post,

    })





def signup(request):



    if request.method =='POST':

        username =request.POST.get('name')
        
        password1 =request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1 == password2:

            if User.objects.filter(username =username).exists():
                                
                return redirect('signup')       
        
            else:
                #Creating  a User 
                user =User.objects.create_user(username =username ,                                                                                    
                                          password =password1)
                user.save()

                login(request,user)
                
                return redirect ('signin')
        else:
            
            return redirect('signup')

    else:
        

        return render(request,'signup.html')


def signin(request):


    if request.method == "POST":
        
        username =request.POST.get('name')
        password =request.POST.get('password')



        user =authenticate(username =username, password =password)

        if user is not None:

            login(request,user)
            return redirect('form')
        
        else:
            
            return redirect('signin')
        


    else:
        return render(request,'signin.html')





# @login_required(login_url='signin')

def Logout(request):

    logout(request)

    return redirect('/signin')



def form(request):
            
            
    if request.method == "POST":

        if request.FILES.get('image') == None:
            pass

        else:
            
            image =request.FILES.get('image')
            
        
        title =request.POST.get('title')

        content =request.POST.get('content')


        post =BlogPost.objects.create(
            author =request.user,
            title=title,
            content =content,
            image =image
        )
        post.save()
    



    return render(request,'details.html',{
                 
            })





def details_blog(request,item):

    post =BlogPost.objects.get(id =item)



    return render(request,'details_post.html',{
        'post':post

    })

"""
lawal
1234
lawalhussein@gmail.com
"""