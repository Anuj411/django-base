from django.db import models

class StateModel(models.Model):
    name = models.CharField(max_length=40)

class CityModel(models.Model):
    name = models.CharField(max_length=40)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="city_set")

class FacilityModel(models.Model):
    name = models.CharField(max_length=20)

class TourPackageModel(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="tours/tour_package")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="tour_package_set")
    facility = models.ManyToManyField(FacilityModel, related_name="tour_package_set")

class HotelModel(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="tours/hotel")
    type = models.PositiveIntegerField()
    tour_package = models.ForeignKey(TourPackageModel, on_delete=models.CASCADE, related_name="hotel_set")

class FlightModel(models.Model):
    from_city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="from_city_flight_set")
    to_city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="to_city_flight_set")
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    tour_package = models.ForeignKey(TourPackageModel, on_delete=models.CASCADE, related_name="flight_set")
