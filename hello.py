


def wsgi_application(environ, start_response):
<<<<<<< HEAD
    status = "200 ОК"
    headers = [ ("Content-Type", "text/plain") ]
=======
    status = bytes("200 ОК", "ascii")
    headers = [ bytes("Content-Type", "ascii"), bytes("text/plain", "ascii") ]
>>>>>>> origin/master
    body = [ bytes(el+"\n", ascii) for el in environ["QUERY_STRING"].split("&") ]
    start_response(status, headers)

    return  body