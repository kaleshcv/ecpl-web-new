from django.urls import path
from .views import homepage,aboutus,certification,infrastructure,contactus,inbound,claimsprocessing,productinformation,ordertaking
from .views import virtual,upselling,tollfree,answer800,ivrservices,customersupport,socialmedia,csr,technicalsupport,helpdesk,remote
from .views import automotive,chemical,education,entertainment,energy,govt,logistics,manufacturing,retailecommerce,telecom,travel,wirelessinternetservice

urlpatterns = [
    path('',homepage),
    path('aboutus',aboutus),
    path('certification',certification),
    path('infrastructure',infrastructure),
    path('contactus',contactus),
    path('inbound',inbound),
    path('claimsprocessing',claimsprocessing),
    path('productinformation',productinformation),
    path('ordertaking',ordertaking),
    path('virtual',virtual),
    path('upselling',upselling),
    path('tollfree',tollfree),
    path('800answering',answer800),
    path('ivrservices',ivrservices),
    path('customersupport',customersupport),
    path('social-media',socialmedia),
    path('csr',csr),
    path('technical-support',technicalsupport),
    path('helpdesk',helpdesk),
    path('remote-IT',remote),
    path('automotive',automotive),
    path('chemical',chemical),
    path('education',education),
    path('entertainment',entertainment),
    path('energy-utilities',energy),
    path('government-agencies',govt),
    path('logistics',logistics),
    path('manufacturing',manufacturing),
    path('retail-ecommerce',retailecommerce),
    path('telecom',telecom),
    path('travel',travel),
    path('wireless-internet-service',wirelessinternetservice),
]
