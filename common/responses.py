from rest_framework.response import Response
from rest_framework import status

headers = {'Content-Type': 'application/json'}

def create_response(message, data, status):
    res = Response(
        data = {'message': message, 'data' : data},
        status=status,
        headers=headers
    )
    return res

def success_response(message='success', data = None, status = status.HTTP_200_OK):
    return create_response(message, data, status)

def failed_response(message='failed', data = None, status = status.HTTP_400_BAD_REQUEST):
    return create_response(message, data, status)
