from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from helpers.token_validate import expired_token
from .models import UserData
from .serializers import ProfileSerializer


class GetUserFromAccessToken(APIView):
    def get(self, request, format=None):
        access_token_str = request.headers.get("Authorization", None)
        if access_token_str is not None:
            access_token_obj = expired_token(access_token_str)
            if access_token_obj is not None:
                user_id = access_token_obj['user_id']
                user = UserData.objects.get(id=user_id)
                serializer = ProfileSerializer(user)
                return Response(serializer.data)

        return (
            Response(
                {"message": "User Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED
            )
        )
