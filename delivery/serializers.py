# delivery/serializers.py

from rest_framework import serializers
from .models import Organization, Item, Pricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'

class DeliveryRequestSerializer(serializers.Serializer):
    zone = serializers.CharField(max_length=50)
    organization_id = serializers.CharField(max_length=10)
    total_distance = serializers.FloatField(min_value=0)
    item_type = serializers.ChoiceField(choices=['perishable', 'non-perishable'])

    def validate(self, data):
        organization_id = data['organization_id']
        zone = data['zone']
        item_type = data['item_type']

        # Check if organization and pricing information exist
        if not Organization.objects.filter(id=organization_id).exists():
            raise serializers.ValidationError("Invalid organization ID")

        if not Pricing.objects.filter(organization_id=organization_id, zone=zone, item__type=item_type).exists():
            raise serializers.ValidationError("Invalid pricing information for the specified organization, zone, and item type")

        return data
