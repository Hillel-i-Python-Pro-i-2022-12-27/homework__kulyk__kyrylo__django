import datetime
from typing import Final

from django.contrib.sessions.backends.cached_db import SessionStore
from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"
KEY__TIME_OF_PREVIOUS_VISIT: Final[str] = "time_of_previous_visit"


class CountOfVisitsView(TemplateView):
    template_name = "count_of_visits/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session

        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[KEY__COUNT_OF_VISITS] = count_of_visits

        time = str(datetime.datetime.now().strftime("%d.%m.%Y | %H:%M:%S"))
        time_of_previous_visit = session.get(KEY__TIME_OF_PREVIOUS_VISIT, "Your first visit!")
        session[KEY__TIME_OF_PREVIOUS_VISIT] = time

        context = super().get_context_data(**kwargs)
        context["title"] = "Count of visits"
        context["count_of_visits"] = count_of_visits
        context["time"] = time
        context["time_of_previous_visit"] = time_of_previous_visit
        return context
