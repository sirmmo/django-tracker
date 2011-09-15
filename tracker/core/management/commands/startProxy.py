from django.core.management.base import NoArgsCommand, CommandError
import sleekxmpp
import datetime
from xml.etree import cElementTree as ET

from settings import TRACKER_RESOURCE_NAME, TRACKER_RESOURCE_SERVER,TRACKER_PROXY_JID ,TRACKER_PROXY_PWD,TRACKER_PROXY_RES ,TRACKER_PROXY_NIC 



class Command(NoArgsCommand):
    help = 'Starts the XMPP Proxy'

    def handle_noargs(self, *args, **options):
        print "proxy startings"
        bot = ProxyBot("%s/%s" % (TRACKER_PROXY_JID, TRACKER_PROXY_RES), TRACKER_PROXY_PWD, TRACKER_PROXY_NIC)
        bot.run()    

class ProxyBot (object):
        def __init__(self, jid, password, nick) :

                self.xmpp = sleekxmpp.ClientXMPP(jid, password)
                self.xmpp.registerPlugin('xep_0004')
                self.xmpp.registerPlugin('xep_0060')
                self.xmpp.registerPlugin('xep_0030')
                self.xmpp.registerPlugin('xep_0199')
                self.jid = jid
                self.nick = nick

                self.xmpp.add_event_handler("session_start", self.handleXMPPConnected)
                self.xmpp.add_event_handler("message", self.handleIncomingMessage)

        def run(self) :
                self.xmpp.connect()
                self.xmpp.process(threaded=False)
        def handleXMPPConnected(self, event):

                self.xmpp.sendPresence(pstatus = "publish to me!!!!!")
                #self.xmpp.plugin['xep_0060'].create_node(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME)
                self.xmpp.plugin['xep_0060'].subscribe(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME)
                print "subscribed"
                #self.xmpp.plugin['xep_0060'].modifyAffiliation(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME, "sensor1@cte.labs.it", "member")
                self.xmpp.plugin['xep_0060'].modifyAffiliation(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME, TRACKER_PROXY_JID, "owner")
                print "affiliation set"
                self.xmpp.sendPresence()
                print "presence sent"

                self.xmpp.plugin['xep_0060'].getItems(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME)

                self.xmpp.plugin['xep_0060'].addItem(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME)
                
        def handleIncomingMessage(self, message) :
                print message['body']
                print self.xmpp.plugin['xep_0060'].getItems(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME)
                el = ET.Element("element")
                el.text = message['body']
                res = self.xmpp.plugin['xep_0060'].addItem(TRACKER_RESOURCE_SERVER, TRACKER_RESOURCE_NAME, [(None, el)])
                print res

