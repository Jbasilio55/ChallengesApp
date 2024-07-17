from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def january(request):
#     return HttpResponse("New Years Resolution, Start working out and get that body on point.")

# def february(request):
#     return HttpResponse("Work on algorithms and become a pro!!")

# def march(request):
#     return HttpResponse("Add More websites to portfolio")

# def april(request):
#     return HttpResponse("learn a new programming language")

# def may(request):
#     return HttpResponse("Go on a date with girlfriend")

# def june(request):
#     return HttpResponse("Go on vacation to Dominican Republic")

# def july(request):
#     return HttpResponse("Start a youtube channel for fun")

# def august(request):
#     return HttpResponse("Win the lottery!!!")

# def september(request):
#     return HttpResponse("Buy a Mansion in California, Miami, and New Jersey")

# def october(request):
#     return HttpResponse("Buy a new super car, Lamborghini Aventador")

# def november(request):
#     return HttpResponse("Buy a Rolex, a patek philip, and AP")

# def december(request):
#     return HttpResponse("Celebrate Birthday with the family")


# def monthly_challenge(request, month):
    # challenge_text = None
    
    # match month:
    #     case "january":
    #         challenge_text = "New Years Resolution, Start working out and get that body on point."
    #     case "february":
    #         challenge_text = "Work on algorithms and become a pro!!"
    #     case "march":
    #         challenge_text = "Add More websites to portfolio"
    #     case "april":
    #         challenge_text = "learn a new programming language"
    #     case "may":
    #         challenge_text = "Go on a date with girlfriend"
    #     case "june":
    #         challenge_text = "Go on vacation to Dominican Republic"
    #     case "july":
    #         challenge_text = "Start a youtube channel for fun"
    #     case "august":
    #         challenge_text = "Win the lottery!!!"
    #     case "september":
    #         challenge_text = "Buy a Mansion in California, Miami, and New Jersey"
    #     case "october":
    #         challenge_text = "Buy a new super car, Lamborghini Aventador"
    #     case "november":
    #         challenge_text = "Buy a Rolex, a patek philip, and AP"
    #     case "december":
    #         challenge_text = "Celebrate Birthday with the family"
    #     case _:
    #         return HttpResponseNotFound("This month is unknown and unsupported")
        
    # return HttpResponse(challenge_text); 
    

#  --------------- Hard coded redirect path -------------------
# def monthly_challenge_by_month(request, month):
#     months = list(monthly_challenges.keys())
    
#     if month > len(months):
#         return HttpResponseNotFound("This month is unknown and unsupported")
#     redirect_month = months[month - 1]
#     return HttpResponseRedirect("/challenges/"+ redirect_month)

monthly_challenges = {
    "january": "New Years Resolution, Start working out and get that body on point.",
    "february": "Work on algorithms and become a pro!!",
    "march": None,
    "april": "learn a new programming language",
    "may": "Go on a date with girlfriend",
    "june": "Go on vacation to Dominican Republic",
    "july": "Start a youtube channel for fun",
    "august": "Win the lottery!!!",
    "september": "Buy a Mansion in California, Miami, and New Jersey",
    "october": "Buy a new super car, Lamborghini Aventador",
    "november": "Buy a Rolex, a patek philip, and AP",
    "december": "Celebrate Birthday with the family",
}

def monthly_challenge_by_month(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("This month is unknown and unsupported")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        return HttpResponseNotFound("<h1>This month is unknown and unsupported</h1>")

# ------------ my version work perfectly fine --------------
# def index(request):
#     months = list(monthly_challenges.keys())
#     response_data = ""
        
#     for month in months:
#         response_data = response_data + f'<h1><a href="{month}">{month.capitalize()}</a></h1><br>'
#     return HttpResponse(response_data)