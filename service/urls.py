from django.urls import path, include
from rest_framework import routers

from service.views import ListCustomer, ListKind, SingleKind, ListEmployee, SingleEmployee, \
    OneSection, SectionGroupView, ServiceAPIView

group_router = routers.SimpleRouter()
group_router.register(r'group',  SectionGroupView)
service_router = routers.SimpleRouter()
service_router.register(r'service', ServiceAPIView)


urlpatterns = [
    path('customer/', ListCustomer.as_view()),
    path('employee/', ListEmployee.as_view()),
    path('employee/<int:id>/', SingleEmployee.as_view()),
    path('kind/', ListKind.as_view()),
    path('kind/<str:name>/', SingleKind.as_view()),
    path('section/<int:id>/', OneSection.as_view()),
    path('section/', include(group_router.urls)),
    path('section/', include(service_router.urls)),
]
