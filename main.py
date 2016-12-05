import os
import json
import falcon
import mimetypes
from wsgiref import simple_server
import json


class Things:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps([{"id": 1, "name": "Thingie"}, {"id": 2, "name": "Thinger"}])

    def on_post(self, req, resp):
        body = req.stream.read()
        params = json.loads(body.decode('utf-8'))
        result = params

        # resp.body = json.dumps(json.JSONEncoder().encode(result))
        resp.body = json.dumps(result)
        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200


app = falcon.API(middleware=[])
app.add_route("/things", Things())

# This part is for convenience in development only
if __name__ == "__main__":
    def static(req, res, static_dir='static', index_file='index.html'):
        path = static_dir + req.path
        if req.path == '/':
            path += index_file
        if os.path.isfile(path):
            res.content_type = mimetypes.guess_type(path)[0]
            res.status = falcon.HTTP_200
            res.stream = open(path)
        else:
            res.status = falcon.HTTP_404


    app.add_sink(static)

    host = "127.0.0.1"
    port = 8888
    httpd = simple_server.make_server(host, port, app)
    print "Serving on %s:%s" % (host, port)
    httpd.serve_forever()
