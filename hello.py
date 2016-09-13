from cgi import parse_qs, escape

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    st_raw = environ['QUERY_STRING']
    st = st_raw.replace("&", "\n")
    print st
    response_body = st
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

