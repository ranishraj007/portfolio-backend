from django.urls import path

from . import views

urlpatterns = [
    path('portfolio/', views.PortfolioDataView.as_view(), name='portfolio-data'),
    path('contact/', views.ContactMessageView.as_view(), name='contact-message'),
    path(
        'admin/messages/',
        views.AdminContactMessagesView.as_view(),
        name='admin-contact-messages',
    ),
]
