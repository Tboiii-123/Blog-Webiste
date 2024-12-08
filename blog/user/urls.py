
from  django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        #Signup
        path('signup/',views.signup ,name='signup'),

#login
        path('signin/',views.signin ,name='signin'),

#logout

        path('logout/',views.Logout , name='logout'),
        
        path('form/',views.form , name='form'),

        path('post_blog/<item>', views.details_blog , name='post_blog')
        
    ]
    

    