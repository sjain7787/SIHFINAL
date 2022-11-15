from distutils.command.config import LANG_EXT
from sre_constants import SUCCESS
from xml.etree.ElementTree import C14NWriterTarget
from django.http import StreamingHttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import BOEwarehousing, Feedback,Import1,Export1,Portaudit,Portoperations,Immigrations,BOEHome,BOEExHome
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.



def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

def service(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request, 'services.html')

def loginuser(request):
    if request.method=="POST":
        username= request.POST.get('Username')
        password= request.POST.get('Password')
        User = authenticate(username=username, password=password)
        if User is not None:
            login(request,User)
            return redirect("/services")
        else:
            return render(request,'login1.html')
    return render(request,'login1.html')



def import1(request):
    if request.user.is_anonymous:
        return redirect("/login")

    #     return redirect("/login")
    if request.method == "POST":
        company = request.POST.get('company')
        vesselid = request.POST.get('vesselid')
        callsign=request.POST.get('callsign')
        cflag=request.POST.get('cflag')
        # datoa=request.POST.get('datoa')
        service=request.POST.get('service')
        arrival=request.POST.get('arrival')
        captain=request.POST.get('captain')
        noc=request.POST.get('noc')
        lc=request.POST.get('lc')
        cio=request.POST.get('cio')
        hdo=request.POST.get('hdo')
        pic=request.POST.get('pic')
        # smembers=request.POST.get('smembers')
        cclear=request.POST.get('cclear')
        bno=request.POST.get('bno')
        tid=request.POST.get('tid')
        amount=request.POST.get('amount')
        fuel=request.POST.get('fuel')
        fq=request.POST.get('fq')
        fquality=request.POST.get('fquality')
        hsp=request.POST.get('hsp')

        import1 = Import1(company=company,vesselid=vesselid,callsign=callsign,cflag=cflag,datoa=datetime.today(),service=service,arrival=arrival,captain=captain,noc=noc,lc=lc,cio=cio,hdo=hdo,pic=pic,cclear=cclear,bno=bno,tid=tid,amount=amount,fuel=fuel,fq=fq,fquality=fquality,hsp=hsp)
        import1.save()    
    return render(request, 'import.html')


def export1(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        company = request.POST.get('company')
        vesselid = request.POST.get('vesselid')
        callsign=request.POST.get('callsign')
        cflag=request.POST.get('cflag')
        # datoa=request.POST.get('datoa')
        service=request.POST.get('service')
        departure=request.POST.get('departure')
        captain=request.POST.get('captain')
        noc=request.POST.get('noc')
        lc=request.POST.get('lc')
        cio=request.POST.get('cio')
        hdo=request.POST.get('hdo')
        pic=request.POST.get('pic')
        smembers=request.POST.get('smembers')
        cclear=request.POST.get('cclear')
        bno=request.POST.get('bno')
        tid=request.POST.get('tid')
        amount=request.POST.get('amount')
        fuel=request.POST.get('fuel')
        fq=request.POST.get('fq')
        fquality=request.POST.get('fquality')
        hsp=request.POST.get('hsp')

        export1 = Export1(company=company,vesselid=vesselid,callsign=callsign,cflag=cflag,datod=datetime.today(),service=service,departure=departure,captain=captain,noc=noc,lc=lc,cio=cio,hdo=hdo,pic=pic,smembers=smembers,cclear=cclear,bno=bno,tid=tid,amount=amount,fuel=fuel,fq=fq,fquality=fquality,hsp=hsp)
        export1.save()    
    return render(request, 'export.html')






def about(request):
    return render(request, 'about.html')

def feedback(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        feedback = Feedback(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        feedback.save()
        messages.success(request,'Your Request has Been Sent!')

    return render(request, 'feedback.html')
    
def shippro(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'shippro.html')


def portoperations(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method=='POST':
        vesselid=request.POST.get('vesselid')
        cbid=request.POST.get('cbid')
        harbourpilot=request.POST.get('harbourpilot')
        tugboatid=request.POST.get('tugboatid')
        vesseloperator=request.POST.get('vesseloperator')
        berthingdock=request.POST.get('berthingdock')
        numberofcontainers=request.POST.get('numberofcontainers')
        cranedriver=request.POST.get('cranedriver')
        type=request.POST.get('type')
        cargo=request.POST.get('cargo')

        portoperations=Portoperations(vesselid=vesselid,cbid=cbid,harbourpilot=harbourpilot,tugboatid=tugboatid,vesseloperator=vesseloperator,berthingdock=berthingdock,numberofcontainers=numberofcontainers,cranedriver=cranedriver,type=type,cargo=cargo)
        portoperations.save()


    return render(request,'portoperations.html')

def employeecorner(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'employeecorner.html')

def logistics(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'logistics.html')

def immigrations(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        name=request.POST.get('name')
        passportnumber=request.POST.get('passportnumber')
        designation=request.POST.get('designation')
        country=request.POST.get('country')
        dateoa=request.POST.get('dateoa')
        workpermit=request.POST.get('workpermit')
        vesselid=request.POST.get('vesselid')


        immigrations = Immigrations(name=name,passportnumber=passportnumber,designation=designation,country=country,dateoa=dateoa,workpermit=workpermit,vesselid=vesselid)
        immigrations.save()    
       
    return render(request, 'immigrations.html')

def customs(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'customs.html')


def boehome(request):
    if request.user.is_anonymous:
        return redirect("/login")
        

    if request.method=="POST":
        portCode=request.POST.get('portCode')
        priorentrystamp=request.POST.get('priorentrystamp')
        importdeptsno=request.POST.get('importdeptsno')
        date=request.POST.get('date')
        customsbrokercode=request.POST.get('customsbrokercode')
        importcode=request.POST.get('importcode')
        importsname=request.POST.get('importsname')
        address=request.POST.get('address')
        vesselsname=request.POST.get('vesselsname')
        rotationnodate=request.POST.get('rotationnodate')
        lineno=request.POST.get('lineno')
        portofshipment=request.POST.get('portofshipment')
        countryoforigin=request.POST.get('countryoforigin')
        coocode=request.POST.get('coocode')
        countryofconsignment=request.POST.get('countryofconsignment')
        coccode=request.POST.get('coccode')
        billofladingdate=request.POST.get('billofladingdate')
        srno=request.POST.get('srno')
        description=request.POST.get('description')
        marksandnumbers=request.POST.get('marksandnumbers')
        unitcode=request.POST.get('unitcode')
        weight=request.POST.get('weight')
        ritcno=request.POST.get('ritcno')
        custrffheading=request.POST.get('custrffheading')
        noofduty=request.POST.get('noofduty')
        assessablevalue=request.POST.get('assessablevalue')
        rate=request.POST.get('rate')
        amount=request.POST.get('amount')
        cetheading=request.POST.get('cetheading')
        addvalue=request.POST.get('addvalue')
        addrate=request.POST.get('addrate')
        totaladdduty=request.POST.get('totaladdduty')
        gstcode=request.POST.get('gstcode')
        igstrate=request.POST.get('igstrate')
        exemptionandnotifiigst=request.POST.get('exemptionandnotifiigst')
        igstamount=request.POST.get('igstamount')
        gstcomprate=request.POST.get('gstcomprate')
        exemptionandnotifigst=request.POST.get('exemptionandnotifigst')
        gstcompamount=request.POST.get('gstcompamount')
        totalduty=request.POST.get('totalduty')

        boehome=BOEHome(portCode=portCode,priorentrystamp=priorentrystamp,importdeptsno=importdeptsno,date=date,customsbrokercode=customsbrokercode,importcode=importcode,importsname=importsname,address=address,vesselsname=vesselsname,rotationnodate=rotationnodate,lineno=lineno,portofshipment=portofshipment,countryoforigin=countryoforigin,coocode=coocode,countryofconsignment=countryofconsignment,coccode=coccode,billofladingdate=billofladingdate,srno=srno,description=description,marksandnumbers=marksandnumbers,unitcode=unitcode,weight=weight,ritcno=ritcno,custrffheading=custrffheading,noofduty=noofduty,assessablevalue=assessablevalue,rate=rate,amount=amount,cetheading=cetheading,addvalue=addvalue,addrate=addrate,totaladdduty=totaladdduty,gstcode=gstcode,igstrate=igstrate,exemptionandnotifiigst=exemptionandnotifiigst,igstamount=igstamount,gstcomprate=gstcomprate,exemptionandnotifigst=exemptionandnotifigst,gstcompamount=gstcompamount,totalduty=totalduty )
        boehome.save()


    return render(request, 'boehome.html')


def boewarehousing(request):
    if request.user.is_anonymous:
        return redirect("/login")
        

    if request.method=="POST":
        portCode=request.POST.get('portCode')
        priorentrystamp=request.POST.get('priorentrystamp')
        importdeptsno=request.POST.get('importdeptsno')
        date=request.POST.get('date')
        customsbrokercode=request.POST.get('customsbrokercode')
        importcode=request.POST.get('importcode')
        importsname=request.POST.get('importsname')
        address=request.POST.get('address')
        vesselsname=request.POST.get('vesselsname')
        rotationnodate=request.POST.get('rotationnodate')
        lineno=request.POST.get('lineno')
        portofshipment=request.POST.get('portofshipment')
        countryoforigin=request.POST.get('countryoforigin')
        coocode=request.POST.get('coocode')
        countryofconsignment=request.POST.get('countryofconsignment')
        coccode=request.POST.get('coccode')
        billofladingdate=request.POST.get('billofladingdate')
        srno=request.POST.get('srno')
        description=request.POST.get('description')
        marksandnumbers=request.POST.get('marksandnumbers')
        unitcode=request.POST.get('unitcode')
        weight=request.POST.get('weight')
        ritcno=request.POST.get('ritcno')
        custrffheading=request.POST.get('custrffheading')
        noofduty=request.POST.get('noofduty')
        assessablevalue=request.POST.get('assessablevalue')
        rate=request.POST.get('rate')
        amount=request.POST.get('amount')
        cetheading=request.POST.get('cetheading')
        mrp=request.POST.get('mrp')
        amountofabatement=request.POST.get('amountofabatement')
        dna=request.POST.get('dna')
        a=request.POST.get('a')
        addrate=request.POST.get('addrate')
        totaladdduty=request.POST.get('totaladdduty')
        gstcode=request.POST.get('gstcode')
        igstrate=request.POST.get('igstrate')
        exemptionandnotifiigst=request.POST.get('exemptionandnotifiigst')
        igstamount=request.POST.get('igstamount')
        gstcomprate=request.POST.get('gstcomprate')
        exemptionandnotifigst=request.POST.get('exemptionandnotifigst')
        gstcompamount=request.POST.get('gstcompamount')
        totalduty=request.POST.get('totalduty')

        boewarehousing=BOEwarehousing(portCode=portCode,priorentrystamp=priorentrystamp,importdeptsno=importdeptsno,date=date,customsbrokercode=customsbrokercode,importcode=importcode,importsname=importsname,address=address,vesselsname=vesselsname,rotationnodate=rotationnodate,lineno=lineno,portofshipment=portofshipment,countryoforigin=countryoforigin,coocode=coocode,countryofconsignment=countryofconsignment,coccode=coccode,billofladingdate=billofladingdate,srno=srno,description=description,marksandnumbers=marksandnumbers,unitcode=unitcode,weight=weight,ritcno=ritcno,custrffheading=custrffheading,noofduty=noofduty,assessablevalue=assessablevalue,rate=rate,amount=amount,cetheading=cetheading,mrp=mrp,amountofabatement=amountofabatement,dna=dna,a=a,addrate=addrate,totaladdduty=totaladdduty,gstcode=gstcode,igstrate=igstrate,exemptionandnotifiigst=exemptionandnotifiigst,igstamount=igstamount,gstcomprate=gstcomprate,exemptionandnotifigst=exemptionandnotifigst,gstcompamount=gstcompamount,totalduty=totalduty )
        boewarehousing.save()


    return render(request, 'boewarehousing.html')

def boeexhome(request):
    if request.user.is_anonymous:
        return redirect("/login")
        

    if request.method=="POST":
        portCode=request.POST.get('portCode')
        priorentrystamp=request.POST.get('priorentrystamp')
        importdeptsno=request.POST.get('importdeptsno')
        date=request.POST.get('date')
        customsbrokercode=request.POST.get('customsbrokercode')
        importcode=request.POST.get('importcode')
        importsname=request.POST.get('importsname')
        address=request.POST.get('address')
        vesselsname=request.POST.get('vesselsname')
        rotationnodate=request.POST.get('rotationnodate')
        lineno=request.POST.get('lineno')
        portofshipment=request.POST.get('portofshipment')
        countryoforigin=request.POST.get('countryoforigin')
        coocode=request.POST.get('coocode')
        countryofconsignment=request.POST.get('countryofconsignment')
        coccode=request.POST.get('coccode')
        billofladingdate=request.POST.get('billofladingdate')
        srno=request.POST.get('srno')
        description=request.POST.get('description')
        marksandnumbers=request.POST.get('marksandnumbers')
        unitcode=request.POST.get('unitcode')
        weight=request.POST.get('weight')
        ritcno=request.POST.get('ritcno')
        custrffheading=request.POST.get('custrffheading')
        noofduty=request.POST.get('noofduty')
        assessablevalue=request.POST.get('assessablevalue')
        rate=request.POST.get('rate')
        amount=request.POST.get('amount')
        cetheading=request.POST.get('cetheading')
        addvalue=request.POST.get('addvalue')
        addrate=request.POST.get('addrate')
        totaladdduty=request.POST.get('totaladdduty')
        gstcode=request.POST.get('gstcode')
        igstrate=request.POST.get('igstrate')
        exemptionandnotifiigst=request.POST.get('exemptionandnotifiigst')
        igstamount=request.POST.get('igstamount')
        gstcomprate=request.POST.get('gstcomprate')
        totalduty=request.POST.get('totalduty')

        boeexhome=BOEExHome(portCode=portCode,priorentrystamp=priorentrystamp,importdeptsno=importdeptsno,date=date,customsbrokercode=customsbrokercode,importcode=importcode,importsname=importsname,address=address,vesselsname=vesselsname,rotationnodate=rotationnodate,lineno=lineno,portofshipment=portofshipment,countryoforigin=countryoforigin,coocode=coocode,countryofconsignment=countryofconsignment,coccode=coccode,billofladingdate=billofladingdate,srno=srno,description=description,marksandnumbers=marksandnumbers,unitcode=unitcode,weight=weight,ritcno=ritcno,custrffheading=custrffheading,noofduty=noofduty,assessablevalue=assessablevalue,rate=rate,amount=amount,cetheading=cetheading,addvalue=addvalue,addrate=addrate,totaladdduty=totaladdduty,gstcode=gstcode,igstrate=igstrate,exemptionandnotifiigst=exemptionandnotifiigst,igstamount=igstamount,gstcomprate=gstcomprate,totalduty=totalduty )
        boeexhome.save()


    return render(request, 'boeexhome.html')


    
def integration(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'integration.html')

        
def auditing(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'auditservice.html')



def companyaudit(request):
    
    if request.user.is_anonymous:
        return redirect("/login")



    return render(request, 'companyaudit.html')



def shipcaudit(request):
    if request.user.is_anonymous:
        return redirect("/login")



    return render(request, 'shipaudit.html')

    
def portcaudit(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method=="POST":
        sname=request.POST.get('sname')
        cname=request.POST.get('cname')
        daudit=request.POST.get('daudit')
        taudit=request.POST.get('taudit')
        naudit=request.POST.get('naudit')
        gstin=request.POST.get('gstin')
        lname=request.POST.get('lname')
        one=request.POST.get('one')
        review1=request.POST.get('review1')
        sugg1=request.POST.get('sugg1')
        two=request.POST.get('two')
        review2=request.POST.get('review2')
        sugg2=request.POST.get('sugg2')
        three=request.POST.get('three')
        review3=request.POST.get('review3')
        sugg3=request.POST.get('sugg3')
        four=request.POST.get('four')
        review4=request.POST.get('review4')
        sugg4=request.POST.get('sugg4')




        portaudit=Portaudit(sname=sname,cname=cname,daudit=daudit,taudit=taudit,naudit=naudit,gstin=gstin,lname=lname,one=one,review1=review1,sugg1=sugg1,two=two,review2=review2,sugg2=sugg2,three=three,review3=review3,sugg3=sugg3,four=four,review4=review4,sugg4=sugg4)
        portaudit.save()
        
    return render(request, 'portaudit.html')

