# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from StudentApp import views

# urlpatterns = [
#     url(r'^student$',views.studentApi),
#     url(r'^student$',views.studentApi),
#     url(r'^student/([0-9]+)$',views.studentApi),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    path('student', views.studentApi),  # Handles GET (all) & POST (create)
    path('student/<int:id>', views.studentApi),  # Handles GET (one), PUT, DELETE
    path('admin', admin.site.urls),  # Admin Panel
]
