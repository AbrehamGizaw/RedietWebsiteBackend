from rest_framework import serializers
from .models import *

class CompanyInfoSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField()
    class Meta:
        model = CompanyInfo
        fields = ['id','name', 'logo', 'hero', 'about', 'created_at', 'updated_at', 'removed_at']
        read_only_fields = ['created_at', 'updated_at', 'removed_at']



class WhyUsSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()
    class Meta:
        model = WhyUs
        fields = ['id','title', 'icon', 'description', 'created_at', 'updated_at', 'removed_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'removed_at']



class ServicesSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()
    class Meta:
        model = Services
        fields = ['id', 'title', 'icon', 'description', 'created_at', 'updated_at', 'removed_at']
        read_only_fields = ['created_at', 'updated_at', 'removed_at']



class TeamSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField()
    class Meta:
        model = Team
        fields = ['id', 'name', 'profession', 'brief_detail', 'years_of_experience', 'contact', 'picture', 'created_at', 'updated_at', 'removed_at']
        read_only_fields = ['created_at', 'updated_at', 'removed_at']



class CompanySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()
    class Meta:
        model = Company
        fields = ['id', 'icon', 'platform', 'value', 'created_at', 'updated_at', 'removed_at']
        read_only_fields = ['created_at', 'updated_at', 'removed_at']



class PartnersSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField()
    class Meta:
        model = Partners
        fields = ['id', 'name', 'logo', 'description', 'created_at', 'updated_at', 'removed_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'removed_at']



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'subject', 'message', ]



class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']



class RelatedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedPost
        fields = ['id', 'title', 'img']

class BlogSerializer(serializers.ModelSerializer):
    related_posts = RelatedPostSerializer(many=True)
    latest_posts = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'img', 'title', 'date', 'description', 'related_posts', 'latest_posts']

    def get_latest_posts(self, obj):
        latest_posts = Blog.objects.exclude(id=obj.id).order_by('-date')[:5] 
        return BlogSerializer(latest_posts, many=True).data
    


class RecentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = RecentUpdate
        fields = ['id', 'picture', 'category', 'title', 'date', 'full_description']
