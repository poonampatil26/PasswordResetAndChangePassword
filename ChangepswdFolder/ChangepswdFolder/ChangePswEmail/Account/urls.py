from django.urls import path
from .views import loginView, registerView, logoutView, homeView, showView, changePassword, simple_upload, model_form_upload
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', loginView, name = 'login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('', homeView, name='home'),
    path('show/', showView, name = 'show'),
    path('chngpwd/', changePassword, name='chngpwd'),
    path('simple_upload/',simple_upload, name = 'simple_upload'),
    path('simple_upload/', simple_upload, name='simple_upload'),
    path('model_form_upload/', model_form_upload, name='model_form_upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)