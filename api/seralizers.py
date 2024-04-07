from rest_framework import serializers
from api.models import Company, Employee

# create serializers
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    Company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields= "__all__"
        
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model= Employee
        fields = "__all__"