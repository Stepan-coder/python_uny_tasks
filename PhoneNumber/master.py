class PhoneNumberException(Exception):
    pass

def chek_leters(tested_string):
 for letter in tested_string:
    if not letter in "01234567890()-+ ":
        return False
 return True


def prepare_phone_number(phone: str)-> str:
    to_remove = [' ', '-', '+', '(', ')']
    if isinstance(phone, str):
        if len(phone) > 10 and chek_leters(phone):
            if phone[:2] == '+7':
                phone_id = phone[2:].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
                new_phone = '+7 (' + phone_id[:3] + ') ' + phone_id[3:6] + '-' + phone_id[6:8] + '-' + phone_id[8:10]
                return new_phone
            elif phone[0] == '8':
                phone_id = phone[1:].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
                new_phone = '+7 (' + phone_id[:3] + ') ' + phone_id[3:6] + '-' + phone_id[6:8] + '-' + phone_id[8:10]
                return new_phone
            else:
                raise PhoneNumberException('PhoneNumber.PhoneNumberException')

prepare_phone_number('+7 ((9122)) 4 6 16 - 88')
