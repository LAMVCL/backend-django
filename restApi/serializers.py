from rest_framework import serializers 
from restApi.models import RestApi
 
 
class RestApiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RestApi
        #Le pasamos los campos a serializar en este caso id y name.
        fields = ('id','name')