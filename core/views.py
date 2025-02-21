from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import CompanyInfo, Company, WhyUs, Team, Partners, Services, Contact, Subscriber, Blog, RecentUpdate
from .serializer import CompanyInfoSerializer, CompanySerializer, WhyUsSerializer, TeamSerializer, PartnersSerializer, ServicesSerializer, ContactSerializer, SubscriberSerializer, BlogSerializer, RecentUpdateSerializer




class CompanyInfoList(APIView):
     def get(self, request):
          companyinfo = CompanyInfo.objects.all()
          serializer = CompanyInfoSerializer(companyinfo, many = True)
          return Response(serializer.data)

# class CompanyInfoCreate(APIView):
#      def post(self, request):
#           serializer = CompanyInfoSerializer(data = request.data)
#           if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data)
#           else:
#                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyInfoDetail(APIView):
     def get_by_pk(self, pk):
          try:
               return CompanyInfo.objects.get(pk=pk)
          except:
               return Response({
                    'error':'There is no such companyinfo'
               }, status=status.HTTP_404_NOT_FOUND )
    
     def get(self, request, pk):
          companyinfo = self.get_by_pk(pk)
          serializer = CompanyInfoSerializer(companyinfo)
          return Response(serializer.data)
     
     def put(self, request, pk):
          companyinfo = self.get_by_pk(pk)
          serializer = CompanyInfoSerializer(companyinfo, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
     
     def delete(self, request, pk):
          companyinfo = self.get_by_pk(pk)
          companyinfo.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


class WhyUsList(APIView):
     def get(self, request):
          whyus = WhyUs.objects.all()
          serializer = WhyUsSerializer(whyus, many = True)
          return Response(serializer.data)

class WhyUsDetail(APIView):
    def get_by_pk(self, pk):
        try:
            return WhyUs.objects.get(pk=pk)
        except WhyUs.DoesNotExist:
            raise NotFound('There is no such companyinfo')

    def get(self, request, pk):
            whyus = self.get_by_pk(pk)
            serializer = WhyUsSerializer(whyus)
            return Response(serializer.data)
        

class ServicesList(APIView):
     def get(self, request):
          services = Services.objects.all()
          serializer = ServicesSerializer(services, many = True)
          return Response(serializer.data)

class TeamList(APIView):
     def get(self, request):
          team = Team.objects.all()
          serializer = TeamSerializer(team, many = True)
          return Response(serializer.data)

class CompanyList(APIView):
     def get(self, request):
          company = Company.objects.all()
          serializer = CompanySerializer(company, many = True)
          return Response(serializer.data)


class PartnersList(APIView):
     def get(self, request):
          partners = Partners.objects.all()
          serializer = PartnersSerializer(partners, many = True)
          filtered_data = [
               {'name': partners['name'],
                'logo' : partners['logo']}
                for partners in serializer.data
          ]
          return Response({"partners":filtered_data})
     
class PartnersDetail(APIView):
     def get(self, request, pk):
          try:
               partners = Partners.objects.get(pk=pk)
          except Partners.DoesNotExist: 
               return Response({
                    'error':'partner not found'
               }, status=status.HTTP_204_NO_CONTENT)

          serializer = PartnersSerializer(partners)
          return Response(serializer.data)


class ContactList(APIView):
     def get(self, request):
          contact = Contact.objects.all()
          serializer = ContactSerializer(contact, many = True)
          return Response(serializer.data)

  
class ContactCreate(APIView):
     def post(self, request):
          serializer = ContactSerializer(data = request.data)
          if serializer.is_valid():
                serializer.save()
                return Response({  "success": True,
                "message": "Your message has been recieved."
            }, status=status.HTTP_201_CREATED)
          return Response({
               "success": False,
               "message": "Something is wrong check it!"
          }, status=status.HTTP_400_BAD_REQUEST)
   
class ContactDetail(APIView):
     def get_by_pk(self, pk):
          try:
               return Contact.objects.get(pk=pk)
          except:
               return Response({
                    'error':'There is no such file'
               }, status=status.HTTP_404_NOT_FOUND )
    
     def get(self, request, pk):
          contact = self.get_by_pk(pk)
          serializer = ContactSerializer(contact)
          return Response(serializer.data)
     

# class SubscriberList(APIView):
#      def get(self, request):
#           subscriber = Subscriber.objects.all()
#           serializer = SubscriberSerializer(subscriber, many = True)
#           return Response(serializer.data)
     

class SubscriberCreate(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            email_address = serializer.validated_data['email']
            if not Subscriber.objects.filter(email=email_address).exists():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Subscription successful."
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "success": False,
                    "message": "Email address already subscribed."
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "success": False,
            "message": "Invalid email address."
        }, status=status.HTTP_400_BAD_REQUEST)


class BlogList(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10  
        blogs = Blog.objects.all()
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class BlogDetail(APIView):
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({
                'error': 'Blog post not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogSerializer(blog)
        return Response(serializer.data)



class RecentUpdateList(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 6  
        updates = RecentUpdate.objects.all()
        for updates in updates:
             updates.short_description = updates.full_description[:100]
        result_page = paginator.paginate_queryset(updates, request)
        serializer = RecentUpdateSerializer(result_page, many=True)
        for item in serializer.data:
             item.pop('full_description', None)
        return paginator.get_paginated_response(serializer.data)


class RecentUpdateDetail(APIView):
    def get(self, request, pk):
        try:
             recent_update = RecentUpdate.objects.get(pk=pk)
        except RecentUpdate.DoesNotExist:
               return Response({
                    'error':'There is no recent updates'
               }, status=status.HTTP_404_NOT_FOUND)
          
        serializer = RecentUpdateSerializer(recent_update)
        return Response(serializer.data)
