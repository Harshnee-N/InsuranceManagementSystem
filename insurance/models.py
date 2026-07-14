from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class Policy(models.Model):
    POLICY_TYPES = [
        ('Health', 'Health Insurance'),
        ('Life', 'Life Insurance'),
        ('Vehicle', 'Vehicle Insurance'),
        ('Home', 'Home Insurance'),
    ]

    name = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=50, choices=POLICY_TYPES)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    duration_years = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomerPolicy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.policy.name}"


class Claim(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    customer_policy = models.ForeignKey(CustomerPolicy, on_delete=models.CASCADE)
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    claim_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Claim {self.id} - {self.status}"