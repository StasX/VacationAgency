from django.db.models import Model, CharField,ForeignKey


# Create your models here.
class UserModel(Model):
    first_name=CharField()
    last_name=CharField()
    email=CharField()
    password=CharField()
    role_id=ForeignKey(Role) 
    class Meta:
        db_table: "users"

#------------------------------------------------------------------------------------------

class RoleModel(Model):
    role_type=CharField()
    def __str__(self):
        return self.role_type
    class Meta:
        db_table: "roles"