from datapeace_app.models import UserData
from datapeace import core_lib
from datapeace_app.forms import UserCreationForm
from django.db.models import Q


def get_users_data(request, raise_exception=True):
    res = core_lib.init_response_dict()

    sort = request.GET.get('sort', '').lower()
    sort_field = sort.lstrip('-')
    if sort_field and sort_field in ['first_name', 'last_name', 'company_name', 'age', 'city', 'state', 'zip', 'email', 'web']:
        if '-' in sort:
            sort_field = '-' + sort_field
    else:
        sort_field = 'first_name'

    name = request.GET.get('name', '')

    try:
        page_no = int(request.GET.get('page', 0))
        if page_no <= 1:
            page_no = 1
    except Exception as ex:
        page_no = 1

    start_page_number = (page_no * 5) - 5
    end_page_number = (page_no * 5)

    try:
        users_data_list = list(UserData.objects.filter(
            Q(first_name__icontains=name) | Q(last_name__icontains=name)).values(
            'id',
            'first_name',
            'last_name',
            'company_name',
            'age',
            'city',
            'state',
            'zip',
            'email',
            'web'
        ).order_by(sort_field))

        limit = int(request.GET.get('limit', len(users_data_list)))

        if limit < len(users_data_list):
            limit = limit
        else:
            limit = len(users_data_list)

        res['cv']['users_data_list'] = users_data_list[:limit][start_page_number:end_page_number]
        res['status'] = True
        return res

    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=raise_exception, print_exception=True,
                                         http_response=False)


def get_user_data_detail(request, user_id, raise_exception=True):
    res = core_lib.init_response_dict()

    try:
        user_data = list(UserData.objects.filter(id=user_id).values(
            'id',
            'first_name',
            'last_name',
            'company_name',
            'age',
            'city',
            'state',
            'zip',
            'email',
            'web'
        ))
        if user_data:
            user_data = user_data[0]
            res['cv']['user_data'] = user_data
            res['status'] = True
            return res
        else:
            res['errors']['__all__'].append(" User Data Not Found")

    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=raise_exception, print_exception=True,
                                         http_response=False)


def create_user(request, data, raise_exception=True):
    res = core_lib.init_response_dict()
    try:

        form = UserCreationForm(data)
        if form.is_valid():

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            company_name = form.cleaned_data.get('company_name')
            age = form.cleaned_data.get('age')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            zip = form.cleaned_data.get('zip')
            email = form.cleaned_data.get('email')
            web = form.cleaned_data.get('web')

            user_data = UserData(
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                age=age,
                city=city,
                state=state,
                zip=zip,
                email=email,
                web=web
            )
            user_data.save()

            res['status'] = True
            res['ticket_id'] = user_data.id
            return res

        else:
            res['errors'] = form.errors
            return res
    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=raise_exception, print_exception=True,
                                         http_response=False)


def edit_user(request, data, user_id, raise_exception=True):
    res = core_lib.init_response_dict()

    try:
        form = UserCreationForm(data)
        user_data = UserData.get_user_by_user_id(user_id)
        if form.is_valid():

            user_data.first_name = form.cleaned_data.get('first_name')
            user_data.last_name = form.cleaned_data.get('last_name')
            user_data.company_name = form.cleaned_data.get('company_name')
            user_data.age = form.cleaned_data.get('age')
            user_data.city = form.cleaned_data.get('city')
            user_data.state = form.cleaned_data.get('state')
            user_data.zip = form.cleaned_data.get('zip')
            user_data.email = form.cleaned_data.get('email')
            user_data.web = form.cleaned_data.get('web')

            user_data.save()

            res['status'] = True
            return res

        else:
            res['errors'] = form.errors
            return res

    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=raise_exception, print_exception=True,
                                         http_response=False)


def delete_user(request, data, user_id, raise_exception=True):
    res = core_lib.init_response_dict()

    try:

        user_data = UserData.get_user_by_user_id(user_id)
        if user_data:
            user_data.delete()

            res['status'] = True
            return res

        else:
            res['errors']['__all__'].append("User Data not found!")
            return res

    except Exception as ex:
        return core_lib.handle_exception(exception_object=ex, raise_exception=raise_exception, print_exception=True,
                                         http_response=False)
