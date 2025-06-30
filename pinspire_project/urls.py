from django.urls import path, include


urlpatterns = [
    # path('admin/', admin.site.urls), # Not using Django Admin with raw SQL
    path('api/', include('account.urls')),
    path('api/', include('core.urls')),
    path('api/', include('user_interactions.urls')),
]
