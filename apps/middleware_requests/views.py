from django.views.generic import ListView

from apps.middleware_requests.models import HttpRequestsLog


class LogListView(ListView):
    model = HttpRequestsLog
    template_name = "middleware_requests/logs/logs_list.html"
    queryset = HttpRequestsLog.objects.all().order_by("-created_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Logs List"
        return context
