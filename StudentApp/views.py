from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student


# 1. @csrf_exempt:
# Disables CSRF protection for this view, which is necessary for APIs accessed by external clients.
# Note: In production, consider using token-based authentication (e.g., JWT) instead of disabling CSRF.

# 2. JSONParser:
# Parses JSON data from the request body into Python dictionaries.

# 3. StudentSerializer:
# Converts Student model instances to JSON (serialization) and JSON data to Student instances (deserialization).

# 4. JsonResponse:
# Returns JSON responses to the client.

@csrf_exempt
def studentApi(request, id=0):

    # Parameters:
    # request: The HTTP request object.

    # id=0: An optional parameter representing the ID of a specific student. Defaults to 0 if not provided.
    if request.method == 'GET':
        # student = Student.objects.all() - fetches all records from the Student table in the database.
        student = Student.objects.all()
        student_serializer = StudentSerializer(
            student, many=True)  # converted into JSON format
        return JsonResponse(student_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request) # Extracts JSON data from the request body, Converts the JSON data into a Python dictionary.
        student_serializer = StudentSerializer(data=student_data) # Converts the Python dictionary into a Student model instance.
        if student_serializer.is_valid(): # Validates the Student model instance.
            student_serializer.save() # Saves the Student model instance to the database.
            return JsonResponse("Added Successfully", safe=False) # Returns a JSON response indicating that the student was added successfully.
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request) # Extracts JSON data from the request body, Converts the JSON data into a Python dictionary.
        student = Student.objects.get(id=id) 
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# What Does views.py Do in Django?
# The views.py file in Django handles HTTP requests and returns responses. It connects the models (database) with the templates (frontend) and processes user requests.

# --------------------------------------------------------------------------------------

# for POST
# 1. JSONParser().parse(request): - Extracts JSON data from the request body, Converts the JSON data into a Python dictionary.

# 2. StudentSerializer(data=student_data): - Takes the parsed data and prepares it for validation, Converts the dictionary into a Django model instance (if valid).

# 3. is_valid() checks if: - All required fields are present, The data types match the model fields(e.g., age must be an integer), Any custom validation rules in the serializer are satisfied.

# student_serializer.save() - Creates a new Student object.


# -------------------------------------------------------------------------------------------