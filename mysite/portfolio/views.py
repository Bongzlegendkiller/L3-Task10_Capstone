from django.shortcuts import render

# Create your views here.

def bongani_portfolio(request):

    """
    Request bongani_portfolio
    
    :param: Request object
    :type: HttpRequest

    :return: bongani.html
    :rtype: HttpResponse

    """
    return render(request,'bongani.html')


