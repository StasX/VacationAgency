from django.db.models import Model, CharField, DateField, FloatField, ForeignKey
from auth.models import UserModel
from datetime import datetime


class VacationModel(Model):
    country = ForeignKey(CountryModel)
    description = CharField(max_length=500)
    start_date = DateField(default=datetime.now)
    end_date = DateField(default=datetime.now)
    price = FloatField(max_digits=7, decimal_places=2)
    image = CharField(max_length=50)

    class Meta:
        db_table = 'vacations'

# ------------------------------------------------------------------------------------------


class CountryModel(Model):
    country = CharField(max_length=50)

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'countries'

# ------------------------------------------------------------------------------------------


class LikeModel(Model):
    user_id = ForeignKey(UserModel)
    vacation_id = ForeignKey(VacationModel)

    class Meta:
        db_table = 'likes'

# ------------------------------------------------------------------------------------------
