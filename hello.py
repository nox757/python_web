


def wsgi_application(environ, start_response):
    status = "200 ОК"
    headers = [ ("Content-Type", "text/plain") ]
    QUERY_STRING = environ["QUERY_STRING"].split("&")
    body = "\n".join(QUERY_STRING)
    start_response(status, headers)

    return [ body ]