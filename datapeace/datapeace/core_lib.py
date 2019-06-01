from __future__ import division
from bson import ObjectId
import traceback
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework import status


def init_response_dict():
    return {'status': False,
            'cv': {},
            'ud': {},
            'errors': {'__all__': list()}}


def generate_unique_object_id():
    return str(ObjectId())


def return_rest_response(data, response_status=status.HTTP_200_OK):
    return Response(data=data, status=response_status)


def return_multi_key_json_response(keys, values, http_response=True):
    data = dict(zip(keys, values))
    if http_response is True:
        return HttpResponse(json.dumps(data))
    else:
        return data


def return_multi_key_json_rest_response(keys, values, rest_response=True, response_status=status.HTTP_200_OK):
    data = dict(zip(keys, values))

    error_description = list()
    if response_status not in [status.HTTP_200_OK, status.HTTP_201_CREATED]:
        if 'errors' in data:
            for key, value in data['errors'].items():
                if type(value) is list:
                    for err in value:
                        error_description.append(err)
                else:
                    error_description.append(value)

        data['error_description'] = error_description if len(error_description) > 0 else ["Something went wrong"]

    if rest_response is True:
        return Response(data=data, status=response_status)
    else:
        return data


def handle_exception(exception_object=None, raise_exception=False, print_exception=False, http_response=True,
                     rest_response=False):
    errors = dict()
    errors['__all__'] = list()

    print(traceback.format_exc())
    errors['__all__'].append(str(exception_object))

    if raise_exception is True and exception_object is not None:
        raise exception_object

    if rest_response is True:
        return return_multi_key_json_rest_response(['errors'], [errors], rest_response,
                                                   response_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif http_response is True:
        return return_multi_key_json_response(['errors'], [errors], http_response)
    else:
        return return_multi_key_json_response(['errors'], [errors], http_response=False)

