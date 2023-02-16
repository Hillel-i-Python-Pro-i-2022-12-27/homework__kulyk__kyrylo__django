from django.views.generic import TemplateView

from apps.example_hw8.services.generate_users import generate_users


class UsersView(TemplateView):
    template_name = "generate_users/generate_users.html"

    def get_context_data(self, amount: int = 10, **kwargs) -> dict:
        context_data = super().get_context_data(amount=amount, **kwargs)

        context_data["title"] = "Users List"

        context_data["users"] = generate_users(amount=amount)

        return context_data
