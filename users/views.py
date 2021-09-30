from django.http import JsonResponse
from allauth.account.views import SignupView, _ajax_response, LoginView


class AjaxSignUpView(SignupView):

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            response = self.form_valid(form)
            return _ajax_response(
                self.request, response, form=form, data=self._get_ajax_data_if())
        else:
            return JsonResponse({'errors': form.errors})


class AjaxLoginView(LoginView):

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            response = self.form_valid(form)
            return _ajax_response(
                self.request, response, form=form, data=self._get_ajax_data_if())
        else:
            return JsonResponse({'errors': form.errors})
# Create your views here.
