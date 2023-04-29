from django.shortcuts import render

tax_rate = 0.15

def index(request):
    return render(request ,"cal_app/index.html")

def greet(request, num):
    x = num * tax_rate
    total_price = x + num
    return render(request ,"cal_app/greet.html" ,{
        "total": total_price,
        "num" : num
    })

def tax_r(request):
    return render(request ,"cal_app/tax.html" ,{
        "taxRate": tax_rate*100
        })