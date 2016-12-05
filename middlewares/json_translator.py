'''
    This middleware will process request and response in the pipeline...
    Usage:
        app = falcon.API(middleware=[JSONTranslator()])
'''
import logging
import falcon
import json

class JSONTranslator(object):

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            # Nothing to do
            return

        body = req.stream.read()
        print (" [M]", json.loads(body.decode('utf-8')))
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['params'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return
        print("[M] return;", req.context['result'])

        resp.body = json.dumps(req.context['result'])