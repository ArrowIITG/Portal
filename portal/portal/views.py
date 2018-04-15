from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # if(request.session["mode"] == '0'):
            return HttpResponseRedirect(reverse("accounts:student_request_form"))
            # else:
            #     return HttpResponseRedirect(reverse("accounts:allrequests"))
        return super().get(request, *args, **kwargs)
