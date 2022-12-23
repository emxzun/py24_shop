from django.core.mail import send_mail


def send_confirmation_email(email, code, title, price):
    full_link = f'http://localhost:8000/api/v1/order/confirm/{code}'

    send_mail(
        f'Привет, подтверди заказ на продукт {title}, на сумму {price}',
        full_link,
        'e352709@gmail.com',
        [email]
    )
