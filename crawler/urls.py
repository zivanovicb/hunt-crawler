from django.conf.urls import url,include
from rest_framework import routers
from .views import Freelancer, Table

urlpatterns = [
    url(r'^([^/]+)', Freelancer.as_view()),
    url(r'^$', Table.as_view()),
    #crapper/ will give the skill table with their ids
    #countries%5B%5D=Serbia&hourly_rate_min=20&hourly_rate_max=30&star_rating=4 url
    # will give you Freelancers from Serbia, with a hourly rate between 20-30 $, and with star rating 4
    #If you want to load users from a second page, add &offset=10(secondpage), or offset=20 for a third page etc.
    #HOWTO use the url
    #hourly_rate_min=10 - hourly rate minimum is 10, hourly_rate_max=20 - hourly rate max is 20
    #countries%5B%5D=Serbia - gives users from Serbia(there can be more than 1 country)
    #star_rating=4 sets the star rating to 4
    #jobs%5B%5D=3 sets the skill  id to 3 which equals to PHP, you can add more than 1 job
    #Connect all of these with a &, as given in the first example.
    #If there are no filters just use crapper/all
]
