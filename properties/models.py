from django.db import models

class Property(models.Model):
    estate_title = models.CharField(max_length=255)
    segment_name = models.CharField(max_length=255, help_text="Segment of the property, e.g., Residential, Commercial")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("sale", "Sale"), ("rent", "Rent")])
    area = models.CharField(max_length=50, help_text="Area of the property, e.g., 2000 sq ft")
    location = models.CharField(max_length=255, help_text="Enter the location of the property")
    latitude = models.FloatField(null=True, blank=True, help_text="Latitude of the property")
    longitude = models.FloatField(null=True, blank=True, help_text="Longitude of the property")
    facilities = models.JSONField(default=list, help_text="Facilities available at the property, e.g., ['living room', 'swimming pool', 'kitchen']")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estate_title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.estate_title}"