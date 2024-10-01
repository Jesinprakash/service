from django.db import models

class Customer(models.Model):

    name=models.CharField(max_length=200)

    phone=models.CharField(max_length=12)

    email=models.EmailField()

    vehicle_number=models.CharField(max_length=200)

    running_kilometer=models.IntegerField()

    status_option=(
        ("pending","pending"),
        ("in progress","in progress")
        ("completed","completed")
    )

    work_status=models.CharField(max_length=200,choices=status_option)

class Work(models.Model):

    customer_object=models.ForeignKey(Customer,on_delete=models.CASCADE)

    description=models.TextField(max_length=200)

    amount=models.FloatField()
