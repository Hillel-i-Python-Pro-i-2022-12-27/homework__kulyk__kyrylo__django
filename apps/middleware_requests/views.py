from django.views.generic import ListView

from apps.middleware_requests.models import HttpRequestsLog


class LogListView(ListView):
    model = HttpRequestsLog
    template_name = "middleware_requests/logs_list.html"
    queryset = HttpRequestsLog.objects.all().order_by("-created_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_all_logs = HttpRequestsLog.objects.count()
        context["title"] = "Logs List"
        context["count_all_logs"] = count_all_logs
        return context
