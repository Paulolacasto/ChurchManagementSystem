from django.db import models

# Model for Church Members
class Member(models.Model):
    GENDER_CHOICES = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Child', 'Child'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()  # Changed to prevent negative values
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)  # Ensures no duplicate phone numbers
    address = models.TextField()
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model for First-Time Visitors
class FirstTimer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)  # Prevents duplicate entries
    invited_by = models.CharField(max_length=100)  # Who invited the visitor
    born_again = models.BooleanField()  # Yes or No
    service_feedback = models.TextField(blank=True, null=True)  # Allows optional feedback
    would_like_visit = models.BooleanField()  # Yes or No
    available_for_fellowship = models.BooleanField()  # Yes or No
    date_visited = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
