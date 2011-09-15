#Django-tracker

Django-tracker is a simple Django application that enables the realtime sending of 
information to the users of a webpage through a simple jabber client.

The architecture is this: 

Your server ==json==> Proxy ==> pubsub ==> Web Clients

The system was tested on eJabberd and works seamlessly

##Installation
set up your jabber server with three users: 

* one publishing its positions 
* one proxy
* one viewer

##Future plans
in next versions the pre-binding should be added.