from django.urls import path
from .views import Login, Register, WalletInfo, DepositFunds, VerifyDeposit, UserListView



urlpatterns = [
    path('register/', Register.as_view(), name= "register"),
    path('login/', Login.as_view(),  name = "login"),
    path ('userlist/',UserListView.as_view(), name = "userlist"),
    path('wallet_info/', WalletInfo.as_view(),name = "wallent"),
    path('deposit/', DepositFunds.as_view(),name = "deposit"),
    path('deposit/verify/<str:reference>/', VerifyDeposit.as_view(),name = "deposit1"),
]

