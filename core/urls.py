from django.urls import path
from .views import CompanyInfoList, CompanyInfoDetail, WhyUsList, WhyUsDetail, ServicesList, TeamList, CompanyList, PartnersList, PartnersDetail, ContactList, ContactCreate, ContactDetail, SubscriberCreate, BlogList, BlogDetail, RecentUpdateList, RecentUpdateDetail

app_name = "core"
urlpatterns = [
    path('company-info-list/', CompanyInfoList.as_view()),
    # path('companyinfocreate/', CompanyInfoCreate.as_view()), 
    path('company-info-detail/<int:pk>', CompanyInfoDetail.as_view()),
    path('why-us-list/', WhyUsList.as_view()),
    path('why-us-detail/<int:pk>', WhyUsDetail.as_view()),
    path('services-list/', ServicesList.as_view()),
    path('team-list/', TeamList.as_view()),
    path('company-list/', CompanyList.as_view()),
    path('partners-list/', PartnersList.as_view()),
    path('partners-detail/<int:pk>', PartnersDetail.as_view()),
    path('contact-list/', ContactList.as_view()),
    path('contact-create/', ContactCreate.as_view()), 
    path('contact-detail/<int:pk>', ContactDetail.as_view()),
    path('blog-list/', BlogList.as_view()),
    path('blog-detail/<int:pk>', BlogDetail.as_view()),
    path('recent-update-list/', RecentUpdateList.as_view()),
    path('recent-update-detail/<int:pk>', RecentUpdateDetail.as_view()),
    # path('subscriberlist/', SubscriberList.as_view()),
    path('subscriber-create/', SubscriberCreate.as_view()),


]