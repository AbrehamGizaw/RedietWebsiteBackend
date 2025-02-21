from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    removed_at = models.DateTimeField(null=True, blank=True, verbose_name="Removed At")

    class Meta:
        abstract = True
        get_latest_by = "created_at"
    
    def soft_deleted(self):
        self.removed_at = timezone.now()
        self.save()
    
    @property
    def is_deleted(self):
        return self.removed_at is not None

class CompanyInfo(BaseModel):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='core/companyinfo', blank=False)
    about = HTMLField()
    hero = HTMLField()

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural= "Companies Informations"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class WhyUs(BaseModel):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='core/whyus', blank=False)
    description = HTMLField()

    class Meta:
        verbose_name = "Why Us"
        verbose_name_plural= "Why Us"
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
class Services(BaseModel):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='core/services', blank=False)
    description = HTMLField()


    class Meta:
        verbose_name = "Services"
        verbose_name_plural= "Services"
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
class Team(BaseModel):
    name = models.CharField(max_length=200)
    proffession = models.CharField(max_length=200)
    brief_detail = HTMLField()
    picture = models.ImageField(upload_to='core/team', blank=False)
    years_of_experience = models.IntegerField()
    contact = models.CharField(max_length=20)


    class Meta:
        verbose_name = "Team"
        verbose_name_plural= "Teams"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Company(BaseModel):
    platform = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='core/contact', blank=False)
    value = HTMLField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural= "Contacts"
    

class Partners(BaseModel):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='core/partners', blank=False)
    description = HTMLField()

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural= "partners"
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = HTMLField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural= "Contacts"
    
    def __str__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural= "Subscribers"
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    date = models.DateField()
    description = models.TextField()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural= "Blogs"


    def __str__(self):
        return self.title

class RelatedPost(models.Model):
    blog = models.ForeignKey(Blog, related_name="related_post", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.URLField()

    class Meta:
        verbose_name = "Related Post"
        verbose_name_plural= "Related Posts"
        ordering = ['title']

    def __str__(self):
        return self.title
    
class RecentUpdate(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    date = models.DateField()
    full_description = models.TextField()

    class Meta:
        verbose_name = "Recent Update"
        verbose_name_plural= "Recent Updates"
        ordering = ['title']

    def __str__(self):
        return self.title


