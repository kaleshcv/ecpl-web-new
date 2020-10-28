from django.shortcuts import render
from .models import Quickcontact
# Create your views here.


def addQuickContact(request):

    if request.method=='POST':
        qc=Quickcontact()
        qc.name = request.POST.get('name')
        qc.email = request.POST.get('email')
        qc.contact = request.POST.get('phone')
        qc.country = request.POST.get('country')
        qc.requirement = request.POST.get('requirement')
        qc.save()
        return render(request,'index.html')
    else:
        pass


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
def phoneanswering(request):
    return render(request,'inbound/phone-answering-services.html')
def medicalanswering(request):
    return render(request,'inbound/medical-answering-services.html')

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
def realestate(request):
    return render(request,'industries/real-estate.html')
def wirelessinternetservice(request):
    return render(request,'industries/wireless-internet-service.html')
def bankingfinancial(request):
    return render(request,'industries/banking-financial.html')
def healthcare(request):
    return render(request,'industries/healthcare.html')


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
def customersatisfaction(request):
    return render(request,'outbound/customer-satisfaction.html')
def appointmentsetting(request):
    return render(request,'outbound/appointment-setting-services.html')

#EMAIL SUPPORT
def emailsupport(request):
    return render(request,'email-support.html')

#CHAT Support
def chatsupport(request):
    return render(request,'chat-support.html')

#OTHER
def catiservice(request):
    return render(request,'cati-service.html')
def cctvmonitoring(request):
    return render(request,'cctv-monitoring.html')
def telemarketing(request):
    return render(request,'telemarketing.html')
def disasterrecovery(request):
    return render(request,'disaster-recovery.html')
def bpaas(request):
    return render(request,'bpaas.html')
def callcenterconsulting(request):
    return render(request,'call-center-consulting-services.html')

def superagentservices(request):
    return render(request,'super-agent-services.html')

def bilingual(request):
    return render(request,'bilingual-call-center.html')


#SERVICES
def bposervices(request):
    return render(request,'bpo-services.html')

#Resources
def videos(request):
    return render(request,'videos.html')
def reference(request):
    return render(request,'reference-letters.html')
def testimonials(request):
    return render(request,'testimonials.html')
def casestudies(request):
    return render(request,'case-studies/case-studies-home.html')

#COVID -19

def bcpcovid(request):
    return render(request,'bcp-covid-19.html')
#FAQ
def faq(request):
    return render(request,'call-center-faqs.html')
def callcenterindia(request):
    return render(request,'call-center-services-india.html')
def callcenterphilippines(request):
    return render(request,'call-center-services-philippines.html')


#otherlinks

def privacy(request):
    return render(request,'privacy.html')

#case studies

def support247(request):
    return render(request,'case-studies/24x7-support.html')
def b2boutboundcallcenterservices(request):
    return render(request,'case-studies/b2b-outbound-call-center-services.html')

def bpostreamlining(request):
    return render(request,'case-studies/bpo-streamlining-operations-scouting-company.html')
def catimarketresearch(request):
    return render(request,'case-studies/cati-market-research-services.html')

def catiserviceshealth(request):
    return render(request, 'case-studies/cati-services-health-insurance-provider.html')
def catisurveyeretailer(request):
    return render(request, 'case-studies/cati-survey-e-retailer.html')
def cctvmonitoringsolutionrestaurant(request):
    return render(request,'case-studies/cctv-monitoring-solution-restaurant.html')
def coldcallingservicesformarket(request):
    return render(request,'case-studies/cold-calling-services-for-market-inteligence-company.html')
def customerfrenchbaker(request):
    return render(request,'case-studies/customer-support-order-taking-for-french-baker.html')
def customizedbpoprocesssolution(request):
    return render(request,'case-studies/customized-bpo-process-solution.html')
def disastergeneral(request):
    return render(request,'case-studies/disaster-recovery-general-insurer.html')
def effectiveukpromotioncompany(request):
    return render(request,'case-studies/effective-inbound-and-outbound-support-for-a-uk-based-safety-promotion-company.html')
def helpingpioneergap(request):
    return render(request,'case-studies/helping-a-us-based-health-care-pioneer-widen-the-expense-profit-gap.html')
def highlyproductivemulti(request):
    return render(request,'case-studies/highly-productive-multi-channel-customer-support-for-a-domain-registry-service-provider.html')
def howwemettheanswering(request):
    return render(request,'case-studies/how-we-met-the-answering-threshold-mandate-of-less-than-20-seconds-for-alberta-insurance-council.html')
def inboundcustomersupport(request):
    return render(request,'case-studies/inbound-customer-support.html')
def inboundtechsupport(request):
    return render(request,'case-studies/inbound-tech-support.html')
def inboundtechnicalsupportdesk(request):
    return render(request,'case-studies/inbound-technical-support-desk.html')
def ithelpdesksolution(request):
    return render(request,'case-studies/it-helpdesk-solution.html')

def leadgenerationaustralian(request):
    return render(request,'case-studies/lead-generation-for-australian-based-mortgage-firm.html')
def mobileapplicationsales(request):
    return render(request,'case-studies/mobile-application-sales-outbound-calling.html')

def multicitytelemarketing(request):
    return render(request,'case-studies/multi-city-telemarketing-services.html')
def ourmultilingualoutbound(request):
    return render(request,'case-studies/our-multilingual-outbound-customer-support-helped-a-global-manufacturer-triple-sales-closing.html')
def ourtelemarketingservices(request):
    return render(request,'case-studies/our-telemarketing-services-helped-smartfoam-increase-appointment-settings-by-50.html')
def outboundforretail(request):
    return render(request,'case-studies/outbound-call-center-for-retail-giant.html')
def outstandingcustomer(request):
    return render(request,'case-studies/outstanding-customer-support-services.html')
def productsalesoutbound(request):
    return render(request,'case-studies/product-sales-outbound-cold-calling.html')
def tier1(request):
    return render(request,'case-studies/tier-1-technical-support-for-aviation-industry.html')


#INBOUND EXTRA

def billingqry(request):
    return render(request,'inbound/billing-queries-services.html')
def inquiryhandling(request):
    return render(request,'inbound/inquiry-handling-services.html')
def insuranceclaimsprocessing(request):
    return render(request,'inbound/insurance-claims-processing-services.html')
def ordermanagement(request):
    return render(request,'inbound/order-management-services.html')

def productrecall(request):
    return render(request,'inbound/product-recall-management-services.html')
def rebateprocessing(request):
    return render(request,'inbound/rebate-processing-services.html')
def reservationbooking(request):
    return render(request,'inbound/reservation-booking-services.html')


