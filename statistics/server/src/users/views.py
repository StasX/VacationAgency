from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import UserModel


@api_view(["GET"])
def total_users(request):
    try:
        total = UserModel.objects.all().count()
        json = {"total_users": total}
        return Response(json)
    except Exception as err:
        json = {"error": str(err)}
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# -------------------------------------------------------
