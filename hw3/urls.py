import views

url_pattern = {
    '/': views.index,
    '/hello': views.hello,
    '/dynamic': views.dynamic,
    '/echo/{}/': views.echo
}
