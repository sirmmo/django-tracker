from django.db import models
from django.core.urlresolvers import reverse

try:
    import json
except:
    import simplejson as json

class SentItem(models.Model):
    moment = models.DateTimeField(auto_now = True)
    data = models.TextField()
    
    def url(self):
        return reverse('core_data', kwargs={'index':self.id})
    
    def to_json(self):
        ret = {}
        ret['time'] = self.moment.isoformat()
        ret['data'] = self.data
        ret['url'] = self.url()
        return json.dumps(ret)
    
    