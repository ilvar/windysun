from django.http import HttpResponsePermanentRedirect

class DomainTransitionMiddleware():
    def process_request(self, request):
        if 'surfersbali.com' in request.get_host():
            return HttpResponsePermanentRedirect('http://surfersbali.ru' + request.path)
        if 'www.surfersbali.ru' in request.get_host():
            return HttpResponsePermanentRedirect('http://surfersbali.ru' + request.path)
