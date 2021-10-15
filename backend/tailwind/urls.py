from django.urls import path

from tailwind.views import TailwindView

urlpatterns = [
    path("", TailwindView.as_view(), name="tailwind-example"),
]
