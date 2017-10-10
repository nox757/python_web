


def wsgi_application(environ, start_response):
    status = '200 ОК'
    headers = [ ('Content-Type', 'text/plain') ]
    body = [ bytes(el+'\n', ascii) for el in environ['QUERY_STRING'].split('&') ]
    start_response(status, headers)

    return  body