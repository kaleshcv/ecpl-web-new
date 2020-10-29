from django.urls import path
from .views import homepage,aboutus,certification,infrastructure,contactus,inbound,claimsprocessing,productinformation,ordertaking
from .views import virtual,upselling,tollfree,answer800,ivrservices,customersupport,socialmedia,csr,technicalsupport,helpdesk,remote
from .views import automotive,chemical,education,entertainment,energy,govt,logistics,manufacturing,retailecommerce,telecom,travel,wirelessinternetservice,realestate,bankingfinancial
from .views import customeracquisitionservices,databaseservices,directmail,marketintelligence,outbound,coldcallingservices,leadgeneration
from .views import customersatisfaction,appointmentsetting
from .views import bposervices,phoneanswering,medicalanswering
from .views import videos,casestudies,reference
from .views import emailsupport,chatsupport
from .views import catiservice,cctvmonitoring,telemarketing,disasterrecovery,bpaas,callcenterconsulting,superagentservices,bilingual
from .views import healthcare,testimonials
from .views import bcpcovid,faq,callcenterindia,callcenterphilippines
from .views import privacy
from .views import support247,b2boutboundcallcenterservices,bpostreamlining,catimarketresearch,catiserviceshealth,catisurveyeretailer,cctvmonitoringsolutionrestaurant
from .views import coldcallingservicesformarket,customerfrenchbaker
from .views import *


urlpatterns = [
    path('',homepage),
    path('aboutus',aboutus),
    path('certification',certification),
    path('infrastructure',infrastructure),
    path('contactus',contactus),
    #QuickContact
    path('addQuickContact',addQuickContact),

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
    path('reference-letters',reference),
    path('testimonials',testimonials),
    path('bpaas',bpaas),
    path('call-center-consulting-services',callcenterconsulting),
    path('super-agent-services',superagentservices),
    path('bilingual-call-center',bilingual),
    path('bcp-covid-19',bcpcovid),
    path('call-center-faqs',faq),
    path('call-center-services-india',callcenterindia),
    path('call-center-services-philippines',callcenterphilippines),
    path('privacy',privacy),
    ##########
    path('24x7-support',support247),
    path('b2b-outbound-call-center-services',b2boutboundcallcenterservices),
    path('bpo-streamlining-operations-scouting-company',bpostreamlining),
    path('cati-market-research-services',catimarketresearch),
    path('cati-services-health-insurance-provider',catiserviceshealth),
    path('cati-survey-e-retailer',catisurveyeretailer),
    path('cctv-monitoring-solution-restaurant',cctvmonitoringsolutionrestaurant),
    path('cold-calling-services-for-market-inteligence-company',coldcallingservicesformarket),
    path('customer-support-order-taking-for-french-baker',customerfrenchbaker),
    path('customized-bpo-process-solution',customizedbpoprocesssolution),
    path('disaster-recovery-general-insurer',disastergeneral),
    path('effective-inbound-and-outbound-support-for-a-uk-based-safety-promotion-company',effectiveukpromotioncompany),
    path('helping-a-us-based-health-care-pioneer-widen-the-expense-profit-gap',helpingpioneergap),
    path('highly-productive-multi-channel-customer-support-for-a-domain-registry-service-provider',highlyproductivemulti),
    path('how-we-met-the-answering-threshold-mandate-of-less-than-20-seconds-for-alberta-insurance-council',howwemettheanswering),
    path('inbound-customer-support',inboundcustomersupport),
    path('inbound-tech-support',inboundtechsupport),
    path('inbound-technical-support-desk',inboundtechnicalsupportdesk),
    path('it-helpdesk-solution',ithelpdesksolution),
    path('lead-generation-for-australian-based-mortgage-firm',leadgenerationaustralian),
    path('mobile-application-sales-outbound-calling',mobileapplicationsales),
    path('multi-city-telemarketing-services',multicitytelemarketing),
    path('our-multilingual-outbound-customer-support-helped-a-global-manufacturer-triple-sales-closing',ourmultilingualoutbound),
    path('our-telemarketing-services-helped-smartfoam-increase-appointment-settings-by-50',ourtelemarketingservices),
    path('outbound-call-center-for-retail-giant',outboundforretail),
    path('outstanding-customer-support-services',outstandingcustomer),
    path('product-sales-outbound-cold-calling',productsalesoutbound),
    path('tier-1-technical-support-for-aviation-industry',tier1),

    path('billing-queries-services',billingqry),
    path('inquiry-handling-services',inquiryhandling), # PENDING
    path('insurance-claims-processing-services',insuranceclaimsprocessing),
    path('order-management-services',ordermanagement),
    path('product-recall-management-services',productrecall),
    path('rebate-processing-services',rebateprocessing),
    path('reservation-booking-services',reservationbooking),

    path('b2b-appointment-setting-services',b2bappointmentsetting),
    path('b2b-lead-generation-services',b2bleadgeneration),
    path('customer-complaint-management-services',customercomplaintmanagement),
    path('customer-follow-up-services',customerfollowup),
    path('customer-loyalty-management-services',customerloyaltymanagement),
    path('debt-collection-services',debtcollection),
    path('dormant-customer-reactivation-services',dormantcustomerreactivation),
    path('information-verification-services',informationverification),
    path('lead-generation-for-startups',leadgenerationstartups),
    path('lead-qualification-services',leadqualification),
    path('product-promotion-services',productpromotion),
    path('real-estate-lead-generation-services',realestateleadgeneration),
    path('subscription-renewal-services',subscriptionrenewal),
    path('telemarketing-lead-generation-services',telemarketingleadgenerationservices),
    path('b2b-cold-calling-services',b2bcoldcallingservices),
    path('b2c-appointment-setting-services',b2cappointmentsetting),
    path('b2c-cold-calling-services',b2ccoldcallingservices),
    path('b2c-lead-generation-services',b2cleadgenerationservices),



]
