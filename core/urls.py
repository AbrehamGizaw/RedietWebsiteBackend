from django.urls import path
from .views import CompanyInfoList, CompanyInfoDetail, WhyUsList, WhyUsDetail, ServicesList, TeamList, CompanyList, PartnersList, PartnersDetail, ContactList, ContactCreate, ContactDetail, SubscriberCreate, BlogList, BlogDetail, RecentUpdateList, RecentUpdateDetail

app_name = "core"
urlpatterns = [
    path('companyinfolist/', CompanyInfoList.as_view()),
    # path('companyinfocreate/', CompanyInfoCreate.as_view()), 
    path('companyinfodetail/<int:pk>', CompanyInfoDetail.as_view()),
    path('whyuslist/', WhyUsList.as_view()),
    path('whyusdetail/<int:pk>', WhyUsDetail.as_view()),
    path('serviceslist/', ServicesList.as_view()),
    path('teamlist/', TeamList.as_view()),
    path('companylist/', CompanyList.as_view()),
    path('partnerslist/', PartnersList.as_view()),
    path('partnersdetail/<int:pk>', PartnersDetail.as_view()),
    path('contactlist/', ContactList.as_view()),
    path('contactcreate/', ContactCreate.as_view()), 
    path('contactdetail/<int:pk>', ContactDetail.as_view()),
    path('bloglist/', BlogList.as_view()),
    path('blogdetail/<int:pk>', BlogDetail.as_view()),
    path('recentupdatelist/', RecentUpdateList.as_view()),
    path('recentupdatedetail/<int:pk>', RecentUpdateDetail.as_view()),
    # path('subscriberlist/', SubscriberList.as_view()),
    path('subscribercreate/', SubscriberCreate.as_view()),


]