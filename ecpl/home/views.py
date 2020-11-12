from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Quickcontact, MainContact,Infographics,Careers,Candidate
from . import forms
# Create your views here.


def careerhome(request):
    careers = Careers.objects.all()
    data={'careers':careers}
    return render(request,'careers-home.html',data)

def careerview(request,pk):
    form = forms.Candidate()

    careers=Careers.objects.get(pk=pk)
    data={'careers':careers,'form':form}
    return render(request,'career-details.html',data)

def addcandidate(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    resume = request.FILES.get('resume')
    candidate = Candidate(name=name, email=email, phone=phone, resume=resume)
    candidate.save()
    messages.success(request, 'Information Submitted !')
    return redirect('careers')



def infographics(request):
    info=Infographics.objects.all()
    data={'info':info}
    return render(request,'infographics-home.html',data)

def infodetails(request,pk):

    infodetails=Infographics.objects.get(pk=pk)
    return render(request,'infographics-details.html',{'infodetails':infodetails})



def addQuickContact(request):

    if request.method=='POST':
        qc=Quickcontact()
        qc.name = request.POST.get('FirstName')
        qc.email = request.POST.get('Email')
        qc.contact = request.POST.get('phone')
        qc.country = request.POST.get('country')
        qc.requirement = request.POST.get('description')
        qc.save()
        messages.success(request,'Information submitted successfully !')
        return redirect('callcenter-calculator')
    else:
        return redirect('ecpl-home')


def addMainContact(request):
    if request.method=='POST':
        mc=MainContact()
        mc.name = request.POST.get('FirstName')
        mc.email = request.POST.get('Email')
        mc.contact = request.POST.get('phone')
        mc.country = request.POST.get('country')
        mc.description = request.POST.get('description')
        mc.company=request.POST.get('Company')
        mc.service1=request.POST.get('service1')
        mc.service2 = request.POST.get('service2')
        mc.service3= request.POST.get('service3')
        mc.service4 = request.POST.get('service4')
        mc.service5 = request.POST.get('service5')
        mc.service6 = request.POST.get('service6')
        mc.service7 = request.POST.get('service7')
        mc.service8 = request.POST.get('service8')
        mc.service9 = request.POST.get('service9')
        mc.service10 = request.POST.get('service10')
        mc.service11 = request.POST.get('service11')
        mc.service12 = request.POST.get('service12')
        mc.attachment=request.FILES.get('attachment')
        mc.save()
        messages.success(request,'Information submitted successfully !')
        return redirect('contact-us')
    else:
        return redirect('ecpl-home')

def callcentercalculator(request):
    return render(request,'callcenter-calculator.html')
def pricing(request):
    return render(request,'pricing.html')

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


#OUTBOUND extra
def b2bappointmentsetting(request):
    return render(request,'outbound/b2b-appointment-setting-services.html')
def b2bleadgeneration(request):
    return render(request,'outbound/b2b-lead-generation-services.html')
def customercomplaintmanagement(request):
    return render(request,'outbound/customer-complaint-management-services.html')
def customerfollowup(request):
    return render(request,'outbound/customer-follow-up-services.html')
def customerloyaltymanagement(request):
    return render(request,'outbound/customer-loyalty-management-services.html')
def debtcollection(request):
    return render(request,'outbound/debt-collection-services.html')
def dormantcustomerreactivation(request):
    return render(request,'outbound/dormant-customer-reactivation-services.html')

def informationverification(request):
    return render(request,'outbound/information-verification-services.html')

def leadgenerationstartups(request):
    return render(request,'outbound/lead-generation-for-startups.html')
def leadqualification(request):
    return render(request,'outbound/lead-qualification-services.html')

def productpromotion(request):
    return render(request,'outbound/product-promotion-services.html')

def realestateleadgeneration(request):
    return render(request,'outbound/real-estate-lead-generation-services.html')

def subscriptionrenewal(request):
    return render(request,'outbound/subscription-renewal-services.html')

def telemarketingleadgenerationservices(request):
    return render(request,'outbound/telemarketing-lead-generation-services.html')

def b2bcoldcallingservices(request):
    return render(request,'outbound/b2b-cold-calling-services.html')

def b2cappointmentsetting(request):
    return render(request,'outbound/b2c-appointment-setting-services.html')
def b2ccoldcallingservices(request):
    return render(request,'outbound/b2c-cold-calling-services.html')
def b2cleadgenerationservices(request):
    return render(request,'outbound/b2c-lead-generation-services.html')

#ARTICLES

def corecustomerservices(request):
    return render(request,'articles/3-core-customer-support-needs-outsource-customer-support-services.html')
def coreelemets(request):
    return render(request,'articles/3-core-elements-for-contact-center-compliance.html')
def waysoutsourcing(request):
    return render(request,'articles/3-ways-outsourcing-transforms-your-customer-experience.html')
def telesales4tips(request):
    return render(request,'articles/4-telesales-tips-to-become-successful-in-2018.html')
def biggest5(request):
    return render(request,'articles/5-biggest-customer-support-failures-that-will-cost-your-business.html')
def cspractice5(request):
    return render(request,'articles/5-customer-service-practices-your-business-could-be-doing-better.html')

def perfect5(request):
    return render(request,'articles/5-perfect-customer-acquisition-strategies-that-will-save-you-big-bucks.html')
def ways6tomake(request):
    return render(request,'articles/6-ways-to-make-your-ivr-more-customer-friendly.html')

def crossandupselling(request):
    return render(request,'articles/cross-selling-and-up-selling-best-practices-for-contact-centers.html')

def howtomanage(request):
    return render(request,'articles/how-to-manage-big-data-in-your-call-center.html')
def keybenefits(request):
    return render(request,'articles/key-benefits-of-virtual-call-centers.html')
def thetoptrends(request):
    return render(request,'articles/the-top-customer-service-trends-in-2018.html')
def tipsivr(request):
    return render(request,'articles/tips-for-creating-effective-ivrs.html')
def topsigns(request):
    return render(request,'articles/top-signs-you-are-heading-for-a-customer-service-disaster.html')
def whatcomprises(request):
    return render(request,'articles/what-comprises-a-strong-customer-service-department.html')

def sitemap(request):
    return render(request,'sitemap.html')