import logging
import datapeace.core_lib as core_lib
from rest_framework import status
import datapeace_app.datapeace_lib as datapeace_lib
from datapeace_app.models import UserData


logger = logging.getLogger(__name__)


def user_data_renderer(request):
    try:
        res = datapeace_lib.get_users_data(request, raise_exception=False)
        if 'status' in res and res['status'] is True:
            return core_lib.return_rest_response(data=res['cv'])
        else:
            return core_lib.return_multi_key_json_rest_response(['errors'],
                                                                [res['errors'] if 'errors' in res else None],
                                                                rest_response=True,
                                                                response_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=False, print_exception=True,
                                         http_response=False, rest_response=True)


def user_data_detail_renderer(request, user_id):
    try:
        res = datapeace_lib.get_user_data_detail(request, user_id,
                                                 raise_exception=False)
        if 'status' in res and res['status'] is True:
            return core_lib.return_rest_response(data=res['cv'])
        else:
            return core_lib.return_multi_key_json_rest_response(['errors'],
                                                                [res['errors'] if 'errors' in res else None],
                                                                rest_response=True,
                                                                response_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=False, print_exception=True,
                                         http_response=False, rest_response=True)


def add_user_data_handler(request):
    try:
        res = datapeace_lib.create_user(request, request.data, raise_exception=False)
        if 'status' in res and res['status'] is True:
            return core_lib.return_multi_key_json_rest_response(['success'],
                                                                ['Saved successfully'],
                                                                rest_response=True,
                                                                response_status=status.HTTP_201_CREATED)
        else:
            return core_lib.return_multi_key_json_rest_response(['errors'],
                                                                [res['errors'] if 'errors' in res else ''],
                                                                rest_response=True,
                                                                response_status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=False, print_exception=True,
                                         http_response=False, rest_response=True)


def edit_user_data_renderer(request, user_id):
    res = core_lib.init_response_dict()
    try:

        user_data = UserData.get_user_by_user_id(user_id)
        user_data = user_data.__dict__
        res['ticket'] = user_data
        res['status'] = True

        if 'status' in res and res['status'] is True:
            return core_lib.return_multi_key_json_rest_response(['success'],
                                                                ['Saved successfully'],
                                                                rest_response=True)
        else:
            return core_lib.return_multi_key_json_rest_response(['errors'],
                                                                [res['errors'] if 'errors' in res else ''],
                                                                rest_response=True,
                                                                response_status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=False, print_exception=True,
                                         http_response=False, rest_response=True)


def edit_user_data_handler(request, user_id):
    try:
        res = datapeace_lib.edit_user(request, request.data, user_id, raise_exception=False)
        if 'status' in res and res['status'] is True:
            return core_lib.return_multi_key_json_rest_response(['success'],
                                                                ['Edited successfully'],
                                                                rest_response=True,
                                                                response_status=status.HTTP_200_OK)
        else:
            return core_lib.return_multi_key_json_rest_response(['errors'],
                                                                [res['errors'] if 'errors' in res else ''],
                                                                rest_response=True,
                                                                response_status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=False, print_exception=True,
                                         http_response=False, rest_response=True)


def delete_user_data_renderer(request, user_id):
    try:
        res = datapeace_lib.delete_user(request, request.data, user_id, raise_exception=False)
        if 'status' in res and res['status'] is True:
            return core_lib.return_multi_key_json_rest_response(['success'],
                                                                ['Deleted successfully'],
                                                                rest_response=True,
                                                                response_status=status.HTTP_200_OK)
        else:
            return core_lib.return_multi_key_json_rest_response(['errors'],
                                                                [res['errors'] if 'errors' in res else ''],
                                                                rest_response=True,
                                                                response_status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=False, print_exception=True,
                                         http_response=False, rest_response=True)
