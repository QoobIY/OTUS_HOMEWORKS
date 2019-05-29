from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.TextField(null=True)
    url = models.CharField(max_length=60)


def generate_products():
    Product.objects.create(
        name='Samsung Galaxy S10e 6/128GB',
        url='main/img/1.webp',
        description="""
        смартфон с Android 9.0
        поддержка двух SIM-карт
        экран 5.8", разрешение 3040x1440
        двойная камера 16 МП/12 МП, автофокус
        """,
        price=38400,
    )
    Product.objects.create(
        name='Xiaomi Mi9 SE 6/64GB',
        url='main/img/2.webp',
        description="""
        смартфон с Android 9.0
        поддержка двух SIM-карт
        экран 5.97", разрешение 2340x1080
        три камеры 48 МП/8 МП/13 МП, автофокус
        """,
        price=20170,
    )
    Product.objects.create(
        name='HUAWEI P Smart (2019) 3/32GB',
        url='main/img/3.webp',
        description="""
        смартфон с Android 9.0
        поддержка двух SIM-карт
        экран 6.21", разрешение 2340x1080
        двойная камера 13 МП/2 МП, автофокус
        """,
        price=11089,
    )
    Product.objects.create(
        name='OPPO A5s',
        url='main/img/4.webp',
        description="""
        смартфон с Android 8.1
        поддержка двух SIM-карт
        экран 6.2", разрешение 1520x720
        двойная камера 13 МП/2 МП, автофокус
        """,
        price=11990,
    )
    Product.objects.create(
        name='Apple iPhone Xr 64GB',
        url='main/img/5.webp',
        description="""
        смартфон с iOS 12
        поддержка двух SIM-карт (nano SIM+eSIM)
        экран 6.1", разрешение 1792x828
        камера 12 МП, автофокус
        """,
        price=47930,
    )
    Product.objects.create(
        name='Яндекс.Телефон',
        url='main/img/6.webp',
        description="""
        смартфон с Android 8.1
        поддержка двух SIM-карт
        экран 5.65", разрешение 2160x1080
        двойная камера 16 МП/5 МП, автофокус
        """,
        price=11688,
    )
    return 'Products sucessfully generated'