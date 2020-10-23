from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')
def certification(request):
    return render(request,'certification.html')
def infrastructure(request):
    return render(request,'infrastructure.html')
def contactus(request):
    return render(request,'contactus.html')

#INBOUND
def inbound(request):
    return render(request,'inbound/inbound.html')
def claimsprocessing(request):
    return render(request,'inbound/claims-processing-services.html')

def productinformation(request):
    return render(request,'inbound/product-information.html')
def ordertaking(request):
    return render(request,'inbound/ordertaking.html')
def virtual(request):
    return render(request,'inbound/virtual.html')
def upselling(request):
    return render(request,'inbound/upselling.html')

def tollfree(request):
    return render(request,'inbound/tollfree.html')
def answer800(request):
    return render(request,'inbound/800-answering-services.html')
def ivrservices(request):
    return render(request,'inbound/ivr-services.html')

def customersupport(request):
    return render(request,'customer-support-services.html')

def socialmedia(request):
    return render(request,'social-media-customer-support-services.html')

def csr(request):
    return render(request,'csr.html')
def technicalsupport(request):
    return render(request,'technical/technical-support.html')
def helpdesk(request):
    return render(request,'technical/help-desk-services.html')
def remote(request):
    return render(request,'technical/remote-it-support-services.html')

#INDUSTRIES

def automotive(request):
    return render(request,'industries/automotive.html')

def chemical(request):
    return render(request,'industries/chemical.html')
def education(request):
    return render(request,'industries/education.html')

def entertainment(request):
    return render(request,'industries/entertainment.html')
def energy(request):
    return render(request,'industries/energy-utilities.html')
def govt(request):
    return render(request,'industries/government-agencies.html')
def logistics(request):
    return render(request,'industries/logistics.html')
def manufacturing(request):
    return render(request,'industries/manufacturing.html')

def retailecommerce(request):
    return render(request,'industries/retail-ecommerce.html')
def telecom(request):
    return render(request,'industries/telecom.html')
def travel(request):
    return render(request,'industries/travel.html')

def wirelessinternetservice(request):
    return render(request,'industries/wireless-internet-service.html')

#OUTBOUND
def customeracquisitionservices(request):
    return render(request,'outbound/customer-acquisition-services.html')
def databaseservices(request):
    return render(request,'outbound/database-services.html')
def directmail(request):
    return render(request,'outbound/direct-mail.html')
def marketintelligence(request):
    return render(request,'outbound/market-intelligence.html')
def outbound(request):
    return render(request,'outbound/outbound-home.html')
def coldcallingservices(request):
    return render(request,'outbound/cold-calling-services.html')
def leadgeneration(request):
    return render(request,'outbound/lead-generation-services.html')


#Resources
def videos(request):
    return render(request,'videos.html')

def casestudies(request):
    return render(request,'case-studies/case-studies-home.html')
