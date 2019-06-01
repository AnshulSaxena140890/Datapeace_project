

# Create your views here.

from rest_framework.views import APIView
import datapeace_app.handlers as user_data_handlers


class ListAddUsersDataView(APIView):

    # List
    def get(self, request, *args, **kwargs):
        res = user_data_handlers.user_data_renderer(request)
        return res

    # Create
    def post(self, request, *args, **kwargs):
        res = user_data_handlers.add_user_data_handler(request)
        return res


class UserDetailEditeDeleteView(APIView):

    # Detail
    def get(self, request, *args, **kwargs):
        res = user_data_handlers.user_data_detail_renderer(request,
                                                           user_id=kwargs['user_id'])
        return res

    # Edit
    def put(self, request, *args, **kwargs):
        res = user_data_handlers.edit_user_data_handler(request, user_id=kwargs['user_id'])
        return res

    # Delete
    def post(self, request, *args, **kwargs):
        res = user_data_handlers.delete_user_data_renderer(request, user_id=kwargs['user_id'])
        return res
