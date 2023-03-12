from collections.abc import Callable

from apps.middleware_requests.models import HttpRequestsLog


class LoggingRequestsMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if HttpRequestsLog.objects.filter(
            request_path=request.build_absolute_uri(),
            session_id=request.session.session_key,
            user_id=request.user.id,
        ).exists():
            result = HttpRequestsLog.objects.get(
                request_path=request.build_absolute_uri(),
                session_id=request.session.session_key,
                user_id=request.user.id,
            )
            result.counter += 1
            result.save()
        else:
            HttpRequestsLog.objects.create(
                request_path=request.build_absolute_uri(),
                session_id=request.session.session_key,
                user_id=request.user.id,
                counter=1,
            )
        return response
