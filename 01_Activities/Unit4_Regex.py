import re


# def validate_uk_postcode(user_input):
#     """A function to validate user post codes inputs using regex match function"""
#
#     return bool(re.match(r"^(((([A-Z][A-Z]{0,1})[0-9][A-Z0-9]{0,1}) {0,}[0-9])[A-Z]{2})$", user_input))
#
#
# test_codes = ["M1 1AA", "M60 1NW", "CR2 6XH", "DN55 1PT", "W1A 1HQ", "EC1A 1BB", "12312asda"]
#
#
# for user_input in test_codes:
#     print(validate_uk_postcode(user_input))


def validate_uk_postcode(user_input):
    """A function to validate user post codes inputs using regex match function"""

    return bool(re.match(r"^(((([A-Z][A-Z]{0,1})[0-9][A-Z0-9]{0,1}) {0,}[0-9])[A-Z]{2})$", user_input))





