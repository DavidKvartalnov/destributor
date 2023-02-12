from django.contrib import admin

from service.models import Section, SectionKind, SectionGroup, Service, Access, Payment, User, Role

admin.site.register(SectionKind)
admin.site.register(Section)
admin.site.register(SectionGroup)
admin.site.register(Service)
admin.site.register(Access)
admin.site.register(Payment)
admin.site.register(User)
admin.site.register(Role)
