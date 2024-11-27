from prometheus_client import Counter

# Counter to track requests
REQUEST_COUNT = Counter('app_request_count', 'Total request count', ['method', 'endpoint'])

class MetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
        return self.get_response(request)