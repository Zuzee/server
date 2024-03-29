from django.views.generic import TemplateView
from django.http import HttpResponse
from toilet.forms import ToiletForm
import json

class AddView(TemplateView):
    template_name = "toilet/add.html"

    def get(self, request):
        form = ToiletForm()
        if request.session.has_key('created_by'):
            form = ToiletForm({
                'created_by':request.session['created_by'],
                'latitude':0,
                'longitude':0,
                })
            #form._meta['created_by'].value = request.session['created_by']
        return self.render_to_response({'form':form})

    def post(self, request):
        form = ToiletForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['created_by'] = form.cleaned_data['created_by']

        else:
            return self.render_to_response({'response':json.dumps({'errors':form.errors})})

        return self.render_to_response({'response':json.dumps({'success':'true'})})
