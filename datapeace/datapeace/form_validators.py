from django.core.validators import RegexValidator

zipcode_validator = RegexValidator(r'^[0-9]{6}$', 'Please provide a valid 6 digit pincode')

website_address_validator = RegexValidator(
    r"^(http(s)?://)?([\w-]+\.)+[\w-]+[.com]+(/[/?%&=]*)?$",'Please provide valid website')
