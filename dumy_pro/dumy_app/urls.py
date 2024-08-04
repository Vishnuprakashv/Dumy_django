from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dumy_app'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('email/', views.email_user, name="email_user"),  
    path('register-user/', views.register_user, name="register_user"),  
    path('login/', views.profile_login, name='login'),
    path('user_page/', views.user_page, name='user_page'),
    path('user_image/', views.user_image, name='user_image'),
    path('forgot-password/', views.forgot_password_view, name='forgot_pass'),
    path('update-password/', views.update_password, name='update_password'),

    # For content path analysis_cont
    path('Users-content', views.users_cont, name='users_content'),
    path('Java-content', views.java_cont, name='java_content'),
    path('Python-content', views.python_cont, name='python_content'),
    path('Data-Analysis-content', views.analysis_cont, name='analysis_content'),
    path('Data-Science-content', views.science_cont, name='science_content'),

    # Python Compiler
    path('run_code/', views.run_code, name='run_code'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
