from django.shortcuts import render
from django.views import View

from .models import TheMainInformation

# Create your views here.


class IndexView(View):
    def get(self, request):
        all_data = TheMainInformation.objects.all()

        return render(request, 'index.html', {
            'index_all_data': all_data,
        })


