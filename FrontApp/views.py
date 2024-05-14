from django.shortcuts import render,redirect
from BackApp.models import CarDB,DriverDB,BlogDB
from FrontApp.models import ReviewDB,BookDB,DriverJobDB,SignUpDB
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# Create your views here.
def IndexPage(request):
    rev = ReviewDB.objects.all()
    data = CarDB.objects.all()
    bdata = BlogDB.objects.all()
    return render(request,"index.html",{'data':data,'bdata':bdata,'rev':rev})

def AboutPage(request):
    rev = ReviewDB.objects.all()
    return render(request,"about.html",{'rev':rev})

def BlogPage(request):
    data = BlogDB.objects.all()
    return render(request,"Blog.html",{'data':data})

def CarPage(request):
    data = CarDB.objects.all()
    return render(request,"Cars.html",{'data':data})

def ContactPage(request):
    return render(request,"Contact.html")

def PricePage(request):
    data = CarDB.objects.all()
    return render(request,"Price.html",{'data':data})

def ServicePage(request):
    return render(request,"Service.html")

def CarSingle(request,scid):
    data = CarDB.objects.get(id=scid)
    card = CarDB.objects.all()
    return render(request,"CarSingle.html",{'data':data,'card':card})


def BlogSingle(request,bid):
    bdata = BlogDB.objects.all()
    data = BlogDB.objects.get(id=bid)
    return render(request,"BlogSingle.html",{'data':data,'bdata':bdata})

def SaveContact(request):
    if request.method=="POST":
        a = request.POST.get('CName')
        b = request.POST.get('CEmail')
        img = request.FILES['Image']
        d = request.POST.get('CReview')
        obj = ReviewDB(Name=a,Email=b,Image=img,Review=d)
        obj.save()
        messages.success(request, "Sent Successfullly")
        return redirect(ContactPage)
def BookingPage(request,bkid):
    data = CarDB.objects.get(id=bkid)
    return render(request,"Booking.html",{'data':data})

def DriverFormPage(request):
    return render(request,"DriverForm.html")

def SaveBooking(request):
    if request.method=="POST":
        a = request.POST.get('BName')
        b = request.POST.get('BEmail')
        z = request.POST.get('BCar')
        c = request.POST.get('BNumber')
        d = request.POST.get('BPickUpL')
        e = request.POST.get('BDropOffL')
        f = request.POST.get('BPickUp')
        g = request.POST.get('BDropOff')
        h = request.POST.get('BPickUpT')
        obj = BookDB(Name=a,Email=b,Number=c,PickUpL=d,DropOffL=e,PickUp=f,DropOff=g,PickUpT=h,Car=z)
        obj.save()
        subject = 'Booking Confirmation'
        message = f'Hi {obj.Name}, your booking for {obj.Car} on {obj.PickUp} successfully completed'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [obj.Email ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, "Booked Successfully")
        return redirect(Paymentpage)

def DriverJobSave(request):
    if request.method=="POST":
        a = request.POST.get('CName')
        b = request.POST.get('CEmail')
        c = request.POST.get('CNumber')
        d = request.POST.get('CExperience')
        e = request.FILES['CResume']
        obj = DriverJobDB(Name=a,Email=b,Number=c,Resume=e,Experience=d)
        obj.save()
        messages.success(request, "Sent Successfully")
        return redirect(IndexPage)

def SignupSigninpage(request):
    return render(request,"SignupSignin.html")

def Paymentpage(request):
    return render(request,"Payment.html")

def SignupPage(request):
    if request.method == "POST":
        n = request.POST.get('SName')
        e = request.POST.get('SEmail')
        p = request.POST.get('SPassword')

        obj = SignUpDB(Name=n, Email=e, Password=p)
        obj.save()
        messages.success(request,"Registered")
        return redirect(SignupSigninpage)

def LoginUser(request):
    if request.method=="POST":
        un = request.POST.get('name')
        pd = request.POST.get('password')
        if SignUpDB.objects.filter(Name=un,Password=pd).exists():
            request.session['Name']=un
            request.session['Password']=pd
            messages.success(request, "Login Successfull")
            return redirect(IndexPage)
        else:
            messages.warning(request, "Username does't exist")
            return redirect(SignupSigninpage)
    messages.error(request, "Incorrect password")
    return redirect(SignupSigninpage)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "Logout Successfully")
    return  redirect(SignupSigninpage)


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'index.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()



