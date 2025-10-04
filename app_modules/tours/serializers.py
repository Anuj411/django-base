from rest_framework import serializers
from .models import HotelModel, TourPackageModel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        self.fields.pop('poster')
        # self.fields.pop('tour_package')
        super().__init__(*args, **kwargs)


class TourPackageSerializer(serializers.ModelSerializer):
    hotel_set = HotelSerializer(many=True)
    # flight_set = FlightSerializer(many=True, required=False)
    # hotel_set = serializers.PrimaryKeyRelatedField(queryset=HotelModel.objects.prefetch_related('tour_package'), many=True)

    class Meta:
        model = TourPackageModel
        fields = '__all__'
        # depth = 1
    
    # def validate_hotel_set(self, value):
    #     print(value)
    #     # if data["hotel_set"].instance == None:
    #     #     raise serializers.ValidationError("Add hotel data !!!")
    #     return value
    
    