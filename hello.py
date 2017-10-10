


def wsgi_application(environ, start_response):
    status = bytes("200 ОК", "ascii")
    headers = [ bytes("Content-Type", "ascii"), bytes("text/plain", "ascii") ]
    body = [ bytes(el+"\n", ascii) for el in environ["QUERY_STRING"].split("&") ]
    start_response(status, headers)

    return  body