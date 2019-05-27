from web_framework.response import response


def index(request):
    return response('index')


def hello(request):
    return response('hello')


def dynamic(request):
    return response('dynamic')


def echo(request, url_data):
    return response('echo', {'CONTENT': url_data[0]})
