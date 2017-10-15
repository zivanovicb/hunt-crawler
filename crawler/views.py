import bs4 as bs
from rest_framework import viewsets
from . import serializers
# Create your views here.
import requests
from . import skillcraper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class Table(APIView):
    jobcont = []
    def get(self,request):
        jobdt = skillcraper.getJobs()
        return Response(jobdt)

class Freelancer(APIView):
  def search(self,offset):
    content = []

    link = 'https://www.freelancer.com/ajax/directory/getFreelancer.php?' + offset
    #hourly_rate_min=20&hourly_rate_max=30&online_only=true'

    r = requests.get(link)
    data = r.json()

    users = data.get('users')
    for user in users:
        usernm = (user.get('username'))
        print usernm
        rating = (user.get('freelancer_reputation'))
        country = (user.get('country'))
        rate = (user.get('hourlyrate'))
        bodytxt = (user.get('about'))
        photosrc = (user.get('logo_url'))
        urlic = 'https://www.freelancer.com/u/' + usernm
        dict = {
            'usernm' : usernm,
            'rating' : rating,
            'url' : urlic,
            'photosrc' : photosrc,
            'ratephr' : rate,
            'bodytxt' : bodytxt,
            'country' : country
            }
        content.append(dict)
    return(content)

  def get(self, request, offset, format=None):
        """
        Return a list of all users.
        """

        kdata = self.search(offset)
        # usernames = ['blab']
        return Response(kdata)
