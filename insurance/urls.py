from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='insurance/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('buy/<int:policy_id>/', views.buy_policy, name='buy_policy'),
    path('claim/<int:customer_policy_id>/', views.make_claim, name='make_claim'),

    path('site-admin/', views.admin_dashboard, name='admin_dashboard'),
    path('site-admin/add-policy/', views.add_policy, name='add_policy'),
    path('site-admin/policies/', views.manage_policies, name='manage_policies'),
    path('site-admin/policies/<int:policy_id>/edit/', views.edit_policy, name='edit_policy'),
    path('site-admin/policies/<int:policy_id>/delete/', views.delete_policy, name='delete_policy'),
    path('site-admin/claims/', views.manage_claims, name='manage_claims'),
    path('site-admin/claims/<int:claim_id>/<str:status>/', views.update_claim_status, name='update_claim_status'),
]
