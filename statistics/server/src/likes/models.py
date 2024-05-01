from django.db.models import Model, ForeignKey, CASCADE
from users.models import UserModel
from vacations.models import VacationModel



class LikeModel(Model):
    user_id = ForeignKey(UserModel, on_delete=CASCADE)
    vacation_id = ForeignKey(VacationModel, on_delete=CASCADE)

    class Meta:
        db_table = 'likes'

# ------------------------------------------------------------------------------------------
