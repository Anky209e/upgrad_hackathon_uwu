from django.shortcuts import render
from django.shortcuts import redirect

from classes.fake_news import predict, get_retrain_data

def index(request):
    context = {}

    if request.method == "POST":
        news = request.POST.get("news")
        prediction = predict(news)
        prediction = list(prediction[0])
        prediction[1] = round(prediction[1]*100,2)

        context["news"] = news
        context["prediction"] = prediction

    return render(request, "index.html", context)

def retrain(request):
    if request.method == "POST":
        news = request.POST["news"]
        pred = request.POST["pred"]
        correct = request.POST["correct"]
        
        if correct == "yes":
            target = (pred == "Real")
        else:
            target = (pred == "Fake")
        
        get_retrain_data(news, int(target))
            
    return redirect("/")



# def predict(news):
#     return "Prediction"