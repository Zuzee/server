from django.views.generic import TemplateView
from django.http import HttpResponse
from toilet.forms import ToiletForm

class AddView(TemplateView):
    template_name = "toilet/add.html"

    def get(self, request):
        form = ToiletForm
        return self.render_to_response({'form':form})
    
    def post(self, request):
        form = ToiletForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return self.render_to_response({'response':{'errors':form.errors}})
        
        return self.render_to_response({'response':{'success':'true'}})
