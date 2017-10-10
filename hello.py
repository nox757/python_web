


def wsgi_application(environ, start_response):
    #need change ok????????
    status = '200 OK'
    headers = [ ('Content-Type', 'text/plain') ]
    body = [ bytes(el+'\n', 'ascii') for el in environ['QUERY_STRING'].split('&') ]
    start_response(status, headers)

    return  body