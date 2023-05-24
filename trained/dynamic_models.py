from django.db import models

def create_dynamic_model(model_name, field_names):
    fields = {}

    # Create fields dynamically based on the field_names list
    for field_name in field_names:
        fields[field_name] = models.CharField(max_length=100)

    # Create the dynamic model class using the type() function
    dynamic_model = type(model_name, (models.Model,), fields)

    # Return the dynamically created model class
    return dynamic_model



