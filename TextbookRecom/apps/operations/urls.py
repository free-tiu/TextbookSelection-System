from django.contrib import admin
from django.urls import path,include

from operations import views

app_name = 'operations'

urlpatterns = [
    path('admin/', admin.site.urls),

    #分发路由
    path('operations/', views.operations, name='operations'),
]
