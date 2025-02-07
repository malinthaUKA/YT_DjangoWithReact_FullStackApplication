from rest_framework import serializers
from StudentApp.models import Student  # Import your model


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Specify the model
        fields = '__all__'  # Include all fields from the model
        # Alternatively, specify specific fields:
        # fields = ['id', 'title', 'content', 'created_at']


# Why Do We Use This Serializer?
# In Django REST framework (DRF), serializers convert complex data types (like Django models) into JSON format so that they can be easily sent over APIs. They also validate and deserialize incoming JSON data before saving it to the database.

# Why Use Serializers?
# ✔ Convert Django Model Instances to JSON (for APIs).
# ✔ Convert JSON Data Back to Django Model Instances (for creating/updating records).
# ✔ Validate Data Before Saving (ensures correct data types).
# ✔ Easier API Development (automatically maps Django models to API responses).
