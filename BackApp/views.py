from django.shortcuts import render,redirect
from BackApp.models import CarDB,DriverDB,BlogDB
from FrontApp.models import BookDB,DriverJobDB,ReviewDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def Index_Page(request):
    data = CarDB.objects.all()
    return render(request,"indexpage.html",{'data':data})

def Driver_Display(request):
    data = DriverDB.objects.all()
    return render(request,"DriverDisplay.html",{'data':data})

def Driver_Add(request):
    return render(request,"DriverAdd.html")

def Blog_Add(request):
    return render(request,"BlogAdd.html")
def DriverJob(request):
    data = DriverJobDB.objects.all()
    return render(request,"DriverApplication.html",{'data':data})

def Blog_Display(request):
    data = BlogDB.objects.all()
    return render(request,"BlogDisplay.html",{'data':data})

def Add_Car(request):
    return render(request,"CarAdd.html")

def Save_car(request):
    if request.method=="POST":
        a = request.POST.get('CName')
        b = request.POST.get('CBrand')
        c = request.POST.get('CPrice')
        d = request.POST.get('CPriceD')
        z = request.POST.get('CPriceDD')
        img = request.FILES['CImage']
        f = request.POST.get('CMileage')
        g = request.POST.get('CTransmission')
        h = request.POST.get('CSeats')
        i = request.POST.get('CLuggage')
        j = request.POST.get('CFuel')
        k = request.POST.get('CDiscription')
        obj = CarDB(ModelName=a,Brand=b,Transmission=g,Price=c,PriceD=d,PriceDD=z,Mileage=f,Seats=h,Luggage=i,Fuel=j,Discription=k,Image=img)
        obj.save()
        messages.success(request, "Success")
        return redirect(Display_car)

def Display_car(request):
    data = CarDB.objects.all()
    return render(request,"CarDisplay.html",{'data':data})
def DisplayEditDelete_car(request):
    data = CarDB.objects.all()
    return render(request,"CarEditDelete.html",{'data':data})

def Edit_Page(request,cid):
    data = CarDB.objects.get(id=cid)
    return render(request,"CarEdit.html",{'data':data})

def Update_car(request,cid):
    if request.method=="POST":
        a = request.POST.get('CName')
        b = request.POST.get('CBrand')
        c = request.POST.get('CPrice')
        d = request.POST.get('CPriceD')
        z = request.POST.get('CPriceDD')
        f = request.POST.get('CMileage')
        g = request.POST.get('CTransmission')
        h = request.POST.get('CSeats')
        i = request.POST.get('CLuggage')
        j = request.POST.get('CFuel')
        k = request.POST.get('CDiscription')
        try:
            img = request.FILES['CImage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CarDB.objects.get(id=cid).Image
        CarDB.objects.filter(id=cid).update(ModelName=a,Brand=b,Transmission=g,Price=c,PriceD=d,PriceDD=z,Mileage=f,Seats=h,Luggage=i,Fuel=j,Discription=k,Image=file)
        messages.success(request, "Success")
        return redirect(Display_car)

def Save_driver(request):
    if request.method=="POST":
        a = request.POST.get('DName')
        b = request.POST.get('DAge')
        c = request.POST.get('DLanguage')
        d = request.POST.get('DRating')
        img = request.FILES['DImage']
        f = request.POST.get('DExperience')
        g = request.POST.get('DNumber')
        obj = DriverDB(Name=a,Age=b,Number=g,Language=c,Rating=d,Experience=f,Image=img)
        obj.save()
        messages.success(request, "Success")
        return redirect(Driver_Display)

def Update_Driver(request,did):
    if request.method=="POST":
        a = request.POST.get('DName')
        b = request.POST.get('DAge')
        c = request.POST.get('DLanguage')
        d = request.POST.get('DRating')
        f = request.POST.get('DExperience')
        g = request.POST.get('DNumber')
        try:
            img = request.FILES['DImage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = DriverDB.objects.get(id=did).Image
        DriverDB.objects.filter(id=did).update(Name=a,Age=b,Number=g,Language=c,Rating=d,Experience=f,Image=file)
        messages.success(request, "Success")
        return redirect(Driver_Display)

def Edit_Driver(request,did):
    data = DriverDB.objects.get(id=did)
    return render(request,"DriverEdit.html",{'data':data})

def delete_driver(request,did):
    x = DriverDB.objects.filter(id=did)
    x.delete()
    messages.warning(request, "Deleted")
    return redirect(Driver_Display)
def delete_car(request,cid):
    x = CarDB.objects.filter(id=cid)
    x.delete()
    messages.warning(request, "Deleted")
    return redirect(DisplayEditDelete_car)

def Save_Blog(request):
    if request.method=="POST":
        a = request.POST.get('BHead')
        b = request.POST.get('BSDiscription')
        c = request.POST.get('BDiscription')
        img = request.FILES['BImage']
        obj = BlogDB(Head=a,SDiscription=b,Discription=c,Image=img)
        obj.save()
        messages.success(request, "Success")
        return redirect(Blog_Display)


def Bookings_page(request):
    data = BookDB.objects.all()
    return render(request,"Bookings.html",{'data':data})



def FeedbackPage(request):
    fed = ReviewDB.objects.all()
    return render(request,"Feedback.html",{'fed':fed})

def delete_feed(request,fid):
    x = ReviewDB.objects.filter(id=fid)
    x.delete()
    messages.warning(request, "Deleted")
    return redirect(FeedbackPage)

def LoginPage(request):
    return render(request,"AdminLogin.html")
def Admin_login(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pd = request.POST.get('passwd')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pd)

            if x is not None:
                login(request,x)

                messages.success(request,"Welcome")
                return redirect(Index_Page)
            else:
                messages.error(request,"Incorrect Password")
                return redirect(LoginPage)

        else:
            messages.warning(request, "Please check the username")
            return redirect(LoginPage)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(LoginPage)

