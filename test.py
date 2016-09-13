from cgi import parse_qs, escape

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    st = ""
    for key, val in d.iteritems():
        st = st + key + "=" + str(val[0]) + "<br>"

    response_body = st
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

