from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from parse import search

url_pattern = {}


def check_url(pattern, url):
    global url_pattern
    if url == pattern:
        return True
    if '{}' in pattern:
        if(url[-1] != '/'):
            url += '/'
        return list(search(pattern, url)) if search(pattern, url) else False
    return False


def route(request):
    for url, view in url_pattern.items():
        check = check_url(url, request['url'])
        if check is True:
            return view(request)
        elif check is not False:
            return view(request, check)
    return str.encode('Route {} not founded'.format(request['url']))


def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    request = {'get': parse_qs(environ['QUERY_STRING']), 'url': environ['PATH_INFO']}
    start_response(status, headers)
    return [route(request)]


def run_server(port, urls):
    global url_pattern
    url_pattern = urls
    httpd = make_server('', int(port), simple_app)
    print("Serving on port " + port + "...")
    httpd.serve_forever()
