from django.views.generic import TemplateView
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        # <view logic>
        return HttpResponse('result')