from django.db.models import Model, CharField,ForeignKey


# Create your models here.
class UserModel(Model):
    first_name=CharField(max_length=15)
    last_name=CharField(max_length=15)
    email=CharField(max_length=30)
    password=CharField(max_length=50)
    role_id=ForeignKey(Role) 
    class Meta:
        db_table: "users"

#------------------------------------------------------------------------------------------


class RoleModel(Model):
    role_type=CharField(max_length=20)
    def __str__(self):
        return self.role_type
    class Meta:
        db_table: "roles"