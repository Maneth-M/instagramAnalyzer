class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["cross-origin-resource-policy"] = "cross-origin"
        response["Cross-Origin-Opener-Policy"] = "cross-origin"
        return response

