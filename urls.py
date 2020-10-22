from django.conf.urls import include, url
from rest_framework import routers
from knox import views as knox_views
from .views import (

            
            UserAPI,
           
          
            ChangePasswordAPI,
           
         
            LoginAPI
            
            )

from .views import ValidatePhoneSendOTP, ForgetPasswordChange, ValidateOTP, Register, ValidatePhoneForgot, ForgotValidateOTP

app_name = 'accounts'

# urlpatterns = [
#     url("^", include(router.urls)),
#     url("^auth/register/$", RegistrationAPI.as_view()),
#     url("^auth/login/$", LoginAPI.as_view()),
#     url("^auth/logout/$", knox_views.LogoutView.as_view()),
#     url("^auth/logoutall/$", knox_views.LogoutAllView.as_view()),
#     url("^auth/user/$", UserAPI.as_view()),
#     url("^auth/validate_otp/$", validate_otp),
#     url("^auth/validate_phone/$", validate_phone),
#     url("^auth/change_password/$", ChangePasswordAPI.as_view()),
#     url("^auth/reset_password/$", ResetPasswordAPI.as_view()),
#     url("^auth/forget_password/$", ForgetPasswordAPI.as_view()),
#     url("^auth/user_exists/$", user_existed),
# ]


urlpatterns = [

# for registering a new user

    url("^auth/validate_phone/$", ValidatePhoneSendOTP.as_view()),
    url("^auth/validate_otp/$", ValidateOTP.as_view()),
    url("^auth/register/$", Register.as_view()),

    # for forgot password

    url("^auth/forgot_validate_phone/$", ValidatePhoneForgot.as_view()),
    url("^auth/forgot_validate_otp/$", ForgotValidateOTP.as_view()),
    url("^auth/forgot_password/$", ForgetPasswordChange.as_view()),


    # for login and logout

    url("^auth/login/$", LoginAPI.as_view()),
     url("^auth/logout/$", knox_views.LogoutView.as_view()),
    url("^auth/logoutall/$", knox_views.LogoutAllView.as_view()),

    url("^auth/user/$", UserAPI.as_view()),

]