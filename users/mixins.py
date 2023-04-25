from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")

# not allowing changing password if logged in through github or gmail


class EmailLoginOnlyView(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.login_method == "email"
    
    def handle_no_permission(self):
        messages.error(self.request, "can't go there")
        return redirect("core:home")
