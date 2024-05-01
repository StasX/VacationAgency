from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Count
from .models import LikeModel
from vacations.models import VacationModel

@api_view(["GET"])
def total_likes(request):
    try:
        total = LikeModel.objects.all().count()
        json = {"total_likes": total}
        return Response(json)
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

#-------------------------------------------------------

@api_view(["GET"])
def likes_statistics(request):
    try:
        if LikeModel.objects.all().count()>0:
            likes_by_destination = VacationModel.objects.values('country_id__name') \
                                .annotate(likes_count=Count('likes')) \
                                .order_by()
            json = [{'destination': item['country_id__name'], 'likes': item['likes']} for item in likes_by_destination]
        else:
            json=[]
        return Response(json)
    except Exception  as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

#-------------------------------------------------------
