import re
from base64 import b64encode
import random
import string
from django.utils.text import slugify
from io import BytesIO


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_key_generator(instance):

    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_key_generator(instance)
    return key


def unique_otp_generator(instance):

    key = random.randint(1, 999999)
    print(key)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_otp_generator(instance)
    return key


Dont_use = ['create']


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in Dont_use:
       new_slug = "{slug} - {randstr}".format(
           slug=slug,
           randstr=random_string_generator(size=4)
       )
       return unique_slug_generator(instance, new_slug=new_slug)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug} - {randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
    new_id = random_string_generator()
    k = instance.__class__
    q = k.objects.filter(order_id=new_id).exists()
    if q:
        return unique_order_id_generator(instance)
    return new_id


def phone_validator(phone_number):
    """
    Returns true if phone number is correct else false
    """
    regix = r'^\+?1?\d{10}$'
    com = re.compile(regix)
    find = len(com.findall(phone_number))
    if find == 1:
        return True
    else:
        return False


def password_generator(length):
    """
    Generate fake password of passed length.
    """
    string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(string, length))
    return password


def otp_generator():
    otp = random.randint(999, 9999)
    return otp


def unique_hex_generator(phone: str, password: str):
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'
    salt_int = str(random.randint(1, 999999999999))
    salt_str = "".join(
        [i for i in random.sample(string, random.randint(0, 70))])
    byte_like = bytes(
        str(salt_int+salt_str+str(phone)+password).encode('utf-8'))
    return b64encode(byte_like)
