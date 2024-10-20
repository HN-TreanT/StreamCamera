from rest_framework import permissions
from common import generics_cursor
from django.db import connection


class CustomPermissions(permissions.BasePermission):
    def __init__(self):
       super().__init__()
       
       self.PERMISSION_MAP = {
            'get_list': 'product.view_product',
            'detail_product': 'product.view_product',
            'add_product': 'product.add_product',
            'delete_product': 'product.delete_product',
            'list': 'product.view_product',
            'retrieve': 'product.view_product',
            'create': 'product.add_product',
            'destroy': 'product.delete_product',
            'put':'product.change_product'
        }

    def get_permission_code(self, action):
        return self.PERMISSION_MAP.get(action, None)
       
    def has_permission(self, request, view):
        try:
            if not (request.user and request.user.is_authenticated):
                return False
            permission_code = self.get_permission_code(view.action)
            user_permissions = request.user.get_all_permissions()
            print(permission_code)
            print(user_permissions)
            
            if permission_code in user_permissions:
                return True
            else :
                return False
            # username = request.user
            # # query_String= "SELECT * FROM authenticatorServices_user WHERE is_superuser = 1 AND username = %s"
            # query_String= "SELECT * FROM authenticatorServices_user WHERE username = %s"
            # param = [str(username)]
            # # print(query_String)
            # # print(param)
            # obj = generics_cursor.getDictFromQuery(query_String, param)
            # if len(obj) > 0:
            #     user_permissions = request.user.get_all_permissions()
            #     print("User Permissions: ", user_permissions)
            #     return True
            # else:
            #     return False
        except Exception as e:
            print("Err: ", e)
            return False