import datetime
from typing import Final

from django.contrib.sessions.backends.cached_db import SessionStore
from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"


class CountOfVisitsView(TemplateView):
    template_name = "count_of_visits/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session

        date_time_last_visit = datetime.datetime.now()
        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[KEY__COUNT_OF_VISITS] = count_of_visits

        context = super().get_context_data(**kwargs)
        context["title"] = "Count of visits"
        context["session_id"] = session.session_key
        context["count_of_visits"] = count_of_visits
        context["date_time_last_visit"] = date_time_last_visit
        return context
