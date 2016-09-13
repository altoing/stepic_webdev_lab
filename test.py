from cgi import parse_qs, escape

html = """
<html>
<body>
 a=%(a)s <br>
 b=%(b)s <br>
 c=%(c)s <br>
</body>
</html>
"""

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    for x, y in d.items():
        print x,"=",y[0]

    print d.items()

    a = d.get('a', [''])[0] # Returns the first age value
    b = d.get('b', [''])[0]
    c = d.get('c', [''])[0]


    response_body = html % {
        'a': a,
        'b': b,
        'c': c,
    }

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

