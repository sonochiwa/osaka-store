from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('osaka.urls')),
    path('account/', include('account.urls')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('contact.urls')),
    path('feedback/', include('feedback.urls')),
    # path('send_email/', include('send_email.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)