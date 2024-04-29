from django.db.models import Model, CharField, DateField, DecimalField, ForeignKey, RESTRICT
from datetime import datetime


class CountryModel(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'

# ------------------------------------------------------------------------------------------


class VacationModel(Model):
    country_id = ForeignKey(CountryModel, on_delete=RESTRICT)
    description = CharField(max_length=500)
    start_date = DateField(default=datetime.now)
    end_date = DateField(default=datetime.now)
    price = DecimalField(max_digits=7, decimal_places=2)
    image = CharField(max_length=50)

    class Meta:
        db_table = 'vacations'

# ------------------------------------------------------------------------------------------
