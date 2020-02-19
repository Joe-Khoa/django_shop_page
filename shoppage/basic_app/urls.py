from basic_app import views
from django.conf.urls import url
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'basic_app'

urlpatterns = [
    # re_path(r'',views.index,name = 'index'),
    re_path(r'base$',views.base),
    re_path(r'index$',views.index,name = 'index'),
    re_path(r'about$',views.about,name = 'about'),
    re_path(r'contact$',views.contact,name = 'contact'),
    re_path(r'^categories/(?P<article>[a-zA-Z0-9\-]+)$',views.categories,name = 'categories'),
    re_path(r'faqs$',views.faqs,name = 'faqs'),
    re_path(r'preview/$',views.preview,name = 'preview'),
    re_path(r'cart$',views.cart,name = 'cart'),

    # trap categories to categories_sub "shop/categories/ "+"ipad-pro"
    re_path(r'categories/',views.categories,name = 'categories_sub'),
    # re_path(r'login$',views.login,name = 'login'),
    re_path(r'^detail/(?P<prod>[a-zA-Z0-9\-\(\)\,]+)$',views.detail,name = 'detail'),
    # trap categories to categories_sub "shop/categories/ "+"ipad-pro"
    re_path(r'^detail/',views.detail,name = 'detail_sub'),
    re_path(r'^checkout/$',views.checkout,name = 'checkout'),
    re_path(r'^checkout/(?P<token>[a-zA-Z0-9\-\_]+)$',views.checkout_confirm,name = 'checkout_confirm'),

    re_path(r'^checkout/mail_sent/$',views.checkout_mail_sent,name = 'checkout_mail_sent'),



    #   Authentication
    # re_path(r'sign_up/$',views.sign_up,name='sign_up'),
    # use auth view
    # re_path(r'^login/$',auth_views.LoginView.as_view(template_name='basic_app/login.html'),name='login'),
    # re_path(r'^logout/$',auth_views.LogoutView.as_view(template_name='basic_app/logout.html'),name='logout'),
    # re_path(r'change_password/$',auth_views.PasswordChangeView.as_view(template_name='basic_app/password_change_form.html',success_url='done'),name='password_change'),
    # re_path(r'change_password/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='basic_app/password_change_done.html'),name='password_change_done'),
    # re_path(r'password_reset/$',auth_views.PasswordResetView.as_view(template_name='basic_app/password_reset_form.html',success_url='done'),name='password_reset'),
    # re_path(r'password_reset/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='basic_app/password_reset_done.html'),name='password_reset_done'),
    # re_path(r'reset/<uidb64>/<token>/$',auth_views.PasswordResetConfirmView.as_view(template_name='basic_app/password_reset_confirm.html',success_url='password_reset_complete'),name='password_reset_confirm'),
    # re_path(r'reset/done/$',auth_views.PasswordResetCompleteView.as_view(template_name='basic_app/password_reset_complete.html'),name='password_reset_complete'),
    # url(r'^shop/', include('django.contrib.auth.urls')), # ???


]
