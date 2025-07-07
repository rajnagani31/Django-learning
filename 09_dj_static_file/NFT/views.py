from django.shortcuts import render

# Create your views here.
def NFT_django(req):
    return render(req,'NFT/static.html',{'nm':'Nero'})