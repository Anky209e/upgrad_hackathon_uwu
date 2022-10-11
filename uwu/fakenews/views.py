from django.shortcuts import render
from classes.fake_news import predict

# Create your views here.
def index(request):
    context = {}

    if request.method == "POST":
        news = request.POST.get("news")
        prediction = predict(news)
        prediction = list(prediction[0])
        print(prediction)

        context["news"] = news
        context["prediction"] = prediction

    return render(request, "index.html", context)

def retrain(request):
    print(dict(request.POST))
    
    return redirect("/")



# def predict(news):
#     return "Prediction"