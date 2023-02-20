from django.contrib import admin
from .models import Cryptid, Habitat, Sighting

admin.site.register(Cryptid)
admin.site.register(Habitat)
admin.site.register(Sighting)
# All the models are registered. It is easier for the admin to manage everything
