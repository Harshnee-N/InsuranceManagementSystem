from rest_framework import serializers
from .models import Customer, Policy, Claim

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.customer_name', read_only=True)

    class Meta:
        model = Policy
        fields = ['id', 'customer', 'customer_name', 'policy_type', 'premium', 'expiry_date']


class ClaimSerializer(serializers.ModelSerializer):
    policy_type = serializers.CharField(source='policy.policy_type', read_only=True)
    customer_name = serializers.CharField(source='policy.customer.customer_name', read_only=True)

    class Meta:
        model = Claim
        fields = ['id', 'policy', 'policy_type', 'customer_name', 'claim_amount', 'claim_status']