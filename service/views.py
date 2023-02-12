from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import *
from .serializers import UserSerializer, KindSerializer, KindWithSectionSerializer, \
    SingleSectionSerializer, SectionGroupSerializer, ServiceSerializer


class ListCustomer(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer


class ListEmployee(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer


class SingleEmployee(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    lookup_field = 'id'


class ListKind(generics.ListAPIView):
    queryset = SectionKind.objects.all()
    serializer_class = KindSerializer


class SingleKind(generics.RetrieveAPIView):
    queryset = SectionKind.objects.all()
    serializer_class = KindWithSectionSerializer
    lookup_field = 'name'


class OneSection(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SingleSectionSerializer
    lookup_field = 'id'


class SectionGroupView(viewsets.ModelViewSet):
    queryset = SectionGroup.objects.all()
    serializer_class = SectionGroupSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        new_group = SectionGroup.objects.create(
            name=data['name'],
            section_id=data['section'])
        new_group.save()

        for one_customer in data['customer']:
            customer_obj = User.objects.get(id=one_customer['id'])
            new_group.customer.add(customer_obj)

        serializer = SectionGroupSerializer(new_group)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        pk = kwargs.get('pk')
        one_group = SectionGroup.objects.get(pk=pk)

        one_group.name = data['name']
        one_group.section_id = data['section']
        one_group.save()

        for one_customer in data['customer']:
            customer_obj = User.objects.get(id=one_customer['id'])
            one_group.customer.add(customer_obj)

        return Response("UPDATE IS SUCCESSFUL")


class ServiceAPIView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
