class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["cross-origin-resource-policy"] = "cross-origin"
        response["hello"] = "hi"
        return response

