from django.urls import path
from .views import (
    IndexView,
    SignUpView,
    SignOutView,
    SignInView,
    CustomerList,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

 # <int:pk> captura el ID del usuario para crud
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("staff_sign_up/", SignUpView.as_view(), name="staff_sign_up"),
    path("staff_sign_out/", SignOutView.as_view(), name="staff_sign_out"),
    path("staff_sign_in/", SignInView.as_view(), name="staff_sign_in"),
    path("customer_list/", CustomerList.as_view(), name="customer_list"),
    path(
        "customer_create_view/",
        CustomerCreateView.as_view(),
        name="customer_create_view",
    ),
    path(
        "customer_update_view/<int:pk>/", CustomerUpdateView.as_view(), name="customer_update_view"
    ),  
    path(
        "customer_delete_view/<int:pk>/", CustomerDeleteView.as_view(), name="customer_delete_view"
    ),  
]
