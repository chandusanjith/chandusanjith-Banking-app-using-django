from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import invmm, master, passbook
import random 
import datetime
from django.contrib import messages

def todo(request):
      return render(request, 'todo.html')

def openacc(request):
  return render(request, 'openacc.html')

def createaccno(request):
  f = random.random()
  a = request.POST['firstname']
  b = request.POST['bal']
  c = request.POST['email']
  d = request.POST['phone']
  e = request.POST['message']
  print(a)
  print(b)
  print(c)
  print(d)
  print(e)

  z = master(accountno = f, name = a, openingbal = b, mobilenumber = d, email = c, narration = e)
  z.save()
  
  messages.info(request, f)
  return HttpResponseRedirect('/todo/')


def searchbal(request):
  return render(request, 'checkbal.html')

def checkbal(request):
  global found
  sc = request.POST['accountnumber']
  tableall = master.objects.all()
  total = master.objects.all().count()
  i=0
  print(total)
  print(sc)
  for i in range(total):
    if tableall[i].accountno == sc:
      print(sc)
      print(tableall[i].accountno)
      cubal = tableall[i].openingbal 
      print(cubal) 
      nameimp = tableall[i].name
      print(nameimp)
      print(tableall[i].email)
      print(tableall[i].mobilenumber)
      print(tableall[i].narration)
      context = { 'account': sc ,'name': nameimp, 'balance': cubal}
      return render(request, 'checkbal.html', context)
    else:
       i = i + 1
  return render(request, '404.html')

def dep(request):
  return render(request, 'deposit.html')


def deposit(request):
  a = request.POST['accountnumber']
  b = request.POST['depamt']
  narr = request.POST['message']
  val = master.objects.get(accountno = a)
  prebal = val.openingbal
  prebal = int(prebal)
  b = int(b)
  upbal = 0
  upbal = prebal + b
  upbal = str(upbal)
  master.objects.filter(accountno =a).update(openingbal = upbal)
  datess = datetime.datetime.now()
  name = val.name
  crdrhard = 'CR'
  passb = passbook(accno = a, name = name, balbefore = prebal, balafter = upbal, dateoftran = datess, crdr = crdrhard, narration = narr)
  passb.save()
  return render(request, 'todo.html')

def drw(request):
  return render(request, 'withdraw.html')

def withdraw(request):
  a = request.POST['accountnumber']
  b = request.POST['depamt']
  narr = request.POST['message']
  val = master.objects.get(accountno = a)
  prebal = val.openingbal
  prebal = int(prebal)
  b = int(b)
  upbal = 0
  upbal = prebal - b
  upbal = str(upbal)
  date = datetime.datetime.now()
  name = val.name
  crdr = 'DR'
  master.objects.filter(accountno =a).update(openingbal = upbal)
  passb = passbook(accno = a, name = name, balbefore = prebal, balafter = upbal, dateoftran = date, crdr = crdr, narration = narr)
  passb.save()
  return render(request, 'todo.html')

def psbk(request):
  return render(request, 'passbook.html')


def paschk(request):
  accnumber = request.POST['accountnumber']
  dataget = passbook.objects.filter(accno = accnumber)
  print(dataget)
  return render(request, 'showpass.html',
  {'all_items': dataget})


def sc(request):
  return redirect("https://github.com/chandusanjith/Banking-app-using-django")