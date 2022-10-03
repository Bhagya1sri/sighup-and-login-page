from django.shortcuts import render

# Create your views here.
def register(request):

    if request.method=='post':

     FirstName=request.POST['FirstName']
     LastName=request.POST['LastName']
     ProfilePicture=request.FILES.get('ProfilePicture')
     UserName=request.POST['UserName']
     Email_ID=request.POST['Email_ID']
     Password=request.POST['Password']
     Confirm_password=request.POST['Confirm_password']
     Address=request.POST['Address']

     m=register(FirstName=FirstName,LastName=LastName,ProfilePicture=ProfilePicture,UserName=UserName,Email_ID=Email_ID,Password=Password,Confirm_password=Confirm_password,Address=Address)
     m.save  
     return render(request,'sighup.html')