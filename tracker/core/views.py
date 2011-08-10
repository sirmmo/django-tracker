from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from tracker.core.models import SentItem

import sleekxmpp
#from settings import TRACKER_CLIENT_JID, TRACKER_CLIENT_PWD,TRACKER_BOSH_URL, TRACKER_RESOURCE_SERVER
from settings import TRACKER_CLIENT_JID, TRACKER_CLIENT_PWD,TRACKER_BOSH_URL, TRACKER_RESOURCE_SERVER

def index(request):
    
    #xmpp = sleekxmpp.ClientXMPP(TRACKER_CLIENT_JID, TRACKER_CLIENT_PWD)
    
    return render_to_response("index.html", {
                                             "pwd":TRACKER_CLIENT_PWD,
                                             "jid":TRACKER_CLIENT_JID,
                                             "pubsub":TRACKER_RESOURCE_SERVER, 
                                             "bosh_url":TRACKER_BOSH_URL
                                             })


def data(request, index):
    obj = SentItem.objects.filter(id = index)
    if len(obj) == 1:
        return HttpResponse(obj[0].to_json())
    else:
        return Http404()