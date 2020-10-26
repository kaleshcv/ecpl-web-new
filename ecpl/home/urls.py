from django.urls import path
from .views import homepage,aboutus,certification,infrastructure,contactus,inbound,claimsprocessing,productinformation,ordertaking
from .views import virtual,upselling,tollfree,answer800,ivrservices,customersupport,socialmedia,csr,technicalsupport,helpdesk,remote
from .views import automotive,chemical,education,entertainment,energy,govt,logistics,manufacturing,retailecommerce,telecom,travel,wirelessinternetservice,realestate,bankingfinancial
from .views import customeracquisitionservices,databaseservices,directmail,marketintelligence,outbound,coldcallingservices,leadgeneration
from .views import customersatisfaction,appointmentsetting
from .views import bposervices,phoneanswering,medicalanswering
from .views import videos,casestudies
from .views import emailsupport,chatsupport
from .views import catiservice,cctvmonitoring,telemarketing,disasterrecovery
from .views import healthcare

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
    path('real-estate',realestate),
    path('customer-acquisition-services',customeracquisitionservices),
    path('database-services',databaseservices),
    path('direct-mail',directmail),
    path('market-intelligence',marketintelligence),
    path('videos',videos),
    path('case-studies',casestudies),
    path('outbound-home',outbound),
    path('cold-calling-services',coldcallingservices),
    path('lead-generation',leadgeneration),
    path('customer-satisfaction',customersatisfaction),
    path('appointment-setting-services',appointmentsetting),
    path('email-support',emailsupport),
    path('chat-support',chatsupport),
    path('cati-services',catiservice),
    path('cctv-monitoring',cctvmonitoring),
    path('telemarketing',telemarketing),
    path('bpo-services',bposervices),
    path('phone-answering',phoneanswering),
    path('medical-answering',medicalanswering),
    path('disaster-recovery',disasterrecovery),
    path('banking-financial',bankingfinancial),
    path('healthcare',healthcare),

]
