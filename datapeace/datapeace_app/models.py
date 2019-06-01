from django.db import models
import datapeace.core_lib as core_lib

# Create your models here.


class UserData(models.Model):

    id = models.CharField(max_length=24, primary_key=True, default=core_lib.generate_unique_object_id)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, blank=True, null=True, db_index=True)
    web = models.CharField(max_length=200)

    def __str__(self):
        return str(self.first_name)+" " + str(self.last_name)

    class Meta:

        ordering = ['first_name', 'last_name', 'age']
        verbose_name_plural = 'A. User Data'

    @staticmethod
    def get_user_by_user_id(user_id):
        try:
            return UserData.objects.get(id=user_id)
        except UserData.DoesNotExist:
            return None


class OperationType:
    CREATE = 'C'
    EDIT = 'E'
    DELETE = 'D'