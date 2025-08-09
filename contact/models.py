from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    location = models.CharField(max_length=255, verbose_name="Location")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    fax = models.CharField(
        max_length=20, verbose_name="Fax", blank=True, null=True)
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Infos"

    def __str__(self):
        return f"{self.location} - {self.phone_number}"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=255, verbose_name="Address")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.name
