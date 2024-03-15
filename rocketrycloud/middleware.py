import clubs

class CustomDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.get_host())
        if request.get_host() == 'localhost:8000':
            print('true')
            request.urlconf = clubs.urls
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response