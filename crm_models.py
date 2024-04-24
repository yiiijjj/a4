from django.db import models
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=16)
    zip = models.CharField(max_length=16)
    county = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state} {self.zip}, {self.county} County'
    
class BuildingType(models.Model):
    building_type = models.CharField(max_length=255)

    def __str__(self):
        return self.building_type
    
class Building(models.Model):
    building_type_id = models.ForeignKey(BuildingType, on_delete=models.RESTRICT)
    address_id = models.ForeignKey(Address, on_delete=models.RESTRICT)

    def __str__(self):
        return self.building_type_id

class Vehicle(models.Model):
    year = models.IntegerField(max_length=4)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    VIN = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

class PolicyType(models.Model):
    policy_type = models.CharField(max_length=64)

    def __str__(self):
        return self.policy_type

class Agency(models.Model):
    agency_name = models.CharField(max_length=255)
    address_id = models.ForeignKey(Address, on_delete=models.RESTRICT)

    def __str__(self):
        return self.agency_name
    
class Agent(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address_id = models.ForeignKey(Address, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dob = models.DateField()
    address_id = models.ForeignKey(Address, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)   

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Policy(models.Model):
    policy_name = models.CharField(max_length=255)
    policy_type_id = models.ForeignKey(PolicyType, on_delete=models.RESTRICT)
    agency_id = models.ForeignKey(Agency, on_delete=models.SET_DEFAULT)
    agent_id =  models.ForeignKey(Agent, on_delete=models.SET_DEFAULT)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)
    building_id = models.ForeignKey(Building, on_delete=models.RESTRICT)
    customers = models.ManyToManyField(Customer, through='PolicyCustomer', related_name='policies')

    def __str__(self):
        return self.policy_name
    
class PolicyCustomer(models.Model):
    policy_id = models.ForeignKey(Policy, on_delete=models.RESTRICT)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('customer_id', 'policy_id')

    def __str__(self):
        return f'{self.customer_id.first_name} {self.customer_id.last_name}, {self.policy_id.policy_type_id}{self.policy_id.policy_name}'



