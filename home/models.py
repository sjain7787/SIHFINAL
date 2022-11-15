from pickle import TRUE
from sqlite3 import DataError
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Account(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    DOB=models.DateField()
    gender=models.CharField(
        max_length=25,
        choices=[('Male','Male'),('Female','Female'),('Transgender','Transgender'),('Prefer Not To Say','Prefer Not To Say')]
    ) 
    age=models.IntegerField()
    aadharcard_Number=models.IntegerField()
    address=models.TextField()
    department=models.CharField(max_length=60)
    stakeholderype=models.CharField(max_length=60)
    employeeid=models.CharField(max_length=15)
    place= models.CharField(max_length=60)

    def __str__(self):
        return self.user.username
    





class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name




class Import1(models.Model):
    company  = models.CharField(max_length=122)
    vesselid = models.CharField(max_length=60)
    callsign =models.CharField(max_length=122)
    cflag =models.CharField(max_length=122)
    datoa =models.DateField()
    service =models.CharField(max_length=122)
    arrival =models.CharField(max_length=122)
    captain =models.CharField(max_length=122)
    noc =models.IntegerField()
    lc=models.CharField(max_length=122)
    cio =models.CharField(max_length=122)
    hdo =models.CharField(max_length=122)
    pic =models.CharField(max_length=122)
    smembers =models.TextField()
    cclear =models.CharField(max_length=122)
    bno=models.CharField(max_length=122)
    tid=models.CharField(max_length=122)
    amount=models.IntegerField()
    fuel =models.CharField(max_length=122)
    fq=models.IntegerField()
    fquality=models.IntegerField()
    hsp=models.CharField(max_length=122)



    def __str__(self):
        return self.company



class Export1(models.Model):
    company  = models.CharField(max_length=122)
    vesselid = models.CharField(max_length=60)
    callsign =models.CharField(max_length=122)
    cflag =models.CharField(max_length=122)
    datod =models.DateField()
    service =models.CharField(max_length=122)
    departure =models.CharField(max_length=122)
    captain =models.CharField(max_length=122)
    noc =models.IntegerField()
    lc=models.CharField(max_length=122)
    cio =models.CharField(max_length=122)
    hdo =models.CharField(max_length=122)
    pic =models.CharField(max_length=122)
    smembers =models.TextField()
    cclear =models.CharField(max_length=122)
    bno=models.CharField(max_length=122)
    tid=models.CharField(max_length=122)
    amount=models.IntegerField()
    fuel =models.CharField(max_length=122)
    fq=models.IntegerField()
    fquality=models.CharField(max_length=122)
    hsp=models.CharField(max_length=122)



    def __str__(self):
        return self.company


class Immigrations(models.Model):
    passportnumber=models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    designation = models.CharField(max_length=122)
    country= models.CharField(max_length=122)
    dateoa= models.DateField()
    workpermit = models.CharField(max_length=20)
    vesselid= models.CharField(max_length=122)


    def __str__(self):
        return self.passportnumber
    


class BOEHome(models.Model):
    portCode = models.CharField(max_length=50)
    priorentrystamp = models.CharField(max_length=50)
    importdeptsno = models.IntegerField()
    date = models.DateField()
    customsbrokercode = models.CharField(max_length=50)
    importcode = models.CharField(max_length=50)
    importsname = models.CharField(max_length=50)
    address = models.TextField()
    vesselsname = models.CharField(max_length=50)
    rotationnodate = models.DateField()
    lineno = models.IntegerField()
    portofshipment = models.CharField(max_length=122)
    countryoforigin = models.CharField(max_length=50)
    coocode = models.IntegerField()
    countryofconsignment = models.CharField(max_length=122)
    coccode = models.IntegerField()
    billofladingdate = models.DateField()
    srno = models.IntegerField()
    description = models.TextField()
    marksandnumbers = models.IntegerField()
    unitcode = models.IntegerField()
    weight = models.IntegerField()
    ritcno = models.IntegerField()
    custrffheading = models.TextField()
    noofduty = models.IntegerField()
    assessablevalue = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    cetheading = models.TextField()
    addvalue = models.IntegerField()
    addrate = models.IntegerField()
    totaladdduty = models.IntegerField()
    gstcode = models.IntegerField()
    igstrate = models.IntegerField()
    exemptionandnotifiigst = models.FileField()
    igstamount = models.IntegerField()
    gstcomprate = models.IntegerField()
    exemptionandnotifigst = models.FileField(upload_to='Uploads/')
    gstcompamount = models.IntegerField()
    totalduty = models.IntegerField()


    def __str__(self):
        return self.importcode




class BOEwarehousing(models.Model):
    portCode = models.CharField(max_length=50)
    priorentrystamp = models.CharField(max_length=50)
    importdeptsno = models.IntegerField()
    date = models.DateField()
    customsbrokercode = models.CharField(max_length=50)
    importcode = models.CharField(max_length=50)
    importsname = models.CharField(max_length=50)
    address = models.TextField()
    vesselsname = models.CharField(max_length=50)
    rotationnodate = models.DateField()
    lineno = models.IntegerField()
    portofshipment = models.CharField(max_length=122)
    countryoforigin = models.CharField(max_length=50)
    coocode = models.IntegerField()
    countryofconsignment = models.CharField(max_length=122)
    coccode = models.IntegerField()
    billofladingdate = models.DateField()
    srno = models.IntegerField()
    description = models.TextField()
    marksandnumbers = models.IntegerField()
    unitcode = models.IntegerField()
    weight = models.IntegerField()
    ritcno = models.IntegerField()
    custrffheading = models.TextField()
    noofduty = models.IntegerField()
    assessablevalue = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    cetheading = models.TextField()
    mrp=models.IntegerField(blank=TRUE,default=0)
    amountofabatement=models.IntegerField(blank=True,default=0)
    dna=models.IntegerField()
    a=models.IntegerField()
    addrate = models.IntegerField()
    totaladdduty = models.IntegerField()
    gstcode = models.IntegerField()
    igstrate = models.IntegerField()
    exemptionandnotifiigst = models.FileField()
    igstamount = models.IntegerField()
    gstcomprate = models.IntegerField()
    exemptionandnotifigst = models.FileField(upload_to='Uploads/')
    gstcompamount = models.IntegerField()
    totalduty = models.IntegerField()


    def __str__(self):
        return self.importcode

class BOEExHome(models.Model):
    portCode = models.CharField(max_length=50)
    priorentrystamp = models.CharField(max_length=50)
    importdeptsno = models.IntegerField()
    date = models.DateField()
    customsbrokercode = models.CharField(max_length=50)
    importcode = models.CharField(max_length=50)
    importsname = models.CharField(max_length=50)
    address = models.TextField()
    vesselsname = models.CharField(max_length=50)
    rotationnodate = models.DateField()
    lineno = models.IntegerField()
    portofshipment = models.CharField(max_length=122)
    countryoforigin = models.CharField(max_length=50)
    coocode = models.IntegerField()
    countryofconsignment = models.CharField(max_length=122)
    coccode = models.IntegerField()
    billofladingdate = models.DateField()
    srno = models.IntegerField()
    description = models.TextField()
    marksandnumbers = models.IntegerField()
    unitcode = models.IntegerField()
    weight = models.IntegerField()
    ritcno = models.IntegerField()
    custrffheading = models.TextField()
    noofduty = models.IntegerField()
    assessablevalue = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    cetheading = models.TextField()
    addvalue = models.IntegerField()
    addrate = models.IntegerField()
    totaladdduty = models.IntegerField()
    gstcode = models.IntegerField()
    igstrate = models.IntegerField()
    exemptionandnotifiigst = models.FileField()
    igstamount = models.IntegerField()
    gstcomprate = models.IntegerField()
    totalduty = models.IntegerField()


    def __str__(self):
        return self.importcode


class Portoperations(models.Model):
    vesselid=models.CharField(max_length=20)
    cbid=models.CharField(max_length=30)
    harbourpilot=models.CharField(max_length=50)
    tugboatid=models.CharField(max_length=20)
    vesseloperator=models.CharField(max_length=50)
    berthingdock=models.CharField(max_length=10)
    numberofcontainers=models.IntegerField()
    cranedriver=models.CharField(max_length=50)
    type=models.CharField(max_length=30)
    cargo=models.CharField(max_length=122)



    def __str__(self):
        return self.vesselid



class Portaudit(models.Model):
    sname=models.CharField(max_length=20)
    cname=models.CharField(max_length=60)
    daudit=models.DateField()
    taudit=models.CharField(max_length=30)
    naudit=models.CharField(max_length=30)
    gstin=models.IntegerField()
    lname=models.CharField(max_length=30)
    one=models.CharField(max_length=6)
    review1 = models.TextField(max_length=100)
    sugg1 = models.TextField(max_length=100) 
    two = models.CharField(max_length=100)
    review2 = models.TextField(max_length=100)
    sugg2= models.TextField(max_length=100) 
    three = models.TextField(max_length=100)
    review3 = models.TextField(max_length=100)
    sugg3 = models.TextField(max_length=100) 
    four = models.CharField(max_length=20)
    review4 = models.TextField(max_length=100)
    sugg4 = models.TextField(max_length=100)

    def __str__(self):
        return self.sname

