from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name='logout'), path('admin/', admin.site.urls),
    path('ticket/', views.ticket, name='ticket'),
    path('ticket_detail/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('CreateTicket/', views.CreateTicket, name='CreateTicket'),
    path('home/', views.home, name='home'),
    path('feedback/', views.feedback, name='feedback'),
    path('user_chat/', views.user_chat, name='user_chat'), 
    path('feedback_success/', views.feedback_success, name='feedback_success'), 
    path('package/', views.package, name='package'), 
    path('select/', views.select, name='select'), 
    path('problem/', views.problem, name='problem'), 
    path('chatbot/', views.index, name='chatbot'), 
    path('blog/',include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)