from django.db import models


class Habitat(models.Model):
    country_name = models.CharField(max_length=200)
    continent = models.CharField(max_length=200)

    def __str__(self):
        return self.country_name


class Cryptid(models.Model):
    # The main class for the app
    cryptid_name = models.CharField(max_length=200)
    aggressive = models.BooleanField(True)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE)

    def __str__(self):
        return self.cryptid_name

    # Makes it so calling the instance of the class shows its name instead of the index number.

    def behaviour(self):
        if self.aggressive:
            return "Aggressive"
        else:
            return "Peaceful"

    # Rather than calling the aggressive variable, the app will call this function to make it
    # easier for the user to read the creature's behaviour.

    def get_habitat(self):
        return self.habitat.country_name

    # Gets the cryptid's habitat's name, as calling the habitat may results in showing its index number.


class Sighting(models.Model):
    sighting_site = models.CharField(max_length=200)
    sighting_date = models.DateTimeField('Happened in')
    cryptid = models.ForeignKey(Cryptid, on_delete=models.CASCADE)

    def __str__(self):
        return self.sighting_site

# Create your models here.
