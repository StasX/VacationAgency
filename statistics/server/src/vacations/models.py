from django.db.models import Model, CharField, DateField, FloatField, ForeignKey
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
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'

# ------------------------------------------------------------------------------------------

