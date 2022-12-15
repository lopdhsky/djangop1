from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Sale, Person
from .forms import SaleForm, SaleModelForm

# Create your views here.

def 세일목록(request):
    사람 = Sale.objects.all()
    context = {
        "사람키" : 사람
    }
    return render(request, "newfolder/세일목록.html", context)

def 세일상세(request, pk):
    # print(pk)

    사람 = Sale.objects.get(id=pk)
    # print(세일)

    context = {
        "사람키" : 사람
    }

    return render(request, "newfolder/세일상세.html", context)


def 세일_입력(request):
    폼 = SaleModelForm()
    if request.method == "POST":
        폼 = SaleModelForm(request.POST)
        if 폼.is_valid():
            폼.save()
            # first_name = 폼.cleaned_data['first_name']
            # last_name = 폼.cleaned_data['last_name']
            # age = 폼.cleaned_data['age']
            # person = 폼.cleaned_data['person']

        #     Sale.objects.create(
        #         first_name = first_name,
        #         last_name = last_name,
        #         age = age,
        #         person = person
        #     )

        return redirect("/홈페이지") # 입력후에 다시 홈페이지로 이동


    context = {
        "폼키" : 폼
    }
    return render(request, "newfolder/세일_입력.html", context)


""" shift + alt + a 멀티주석 """
""" def 세일_입력(request):
    폼 = SaleForm()
    if request.method == "POST":
        print("포스트 메소드로 왔네요")
        폼 = SaleForm(request.POST)
        if 폼.is_valid():
            print("유효하네요")
            print(폼.cleaned_data)
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            Sale.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                person = person
            )
            print("세일이 입력 되었습니다.")

            return redirect("/홈페이지") # 입력후에 다시 홈페이지로 이동


    context = {
        "폼키" : 폼
    }
    return render(request, "newfolder/세일_입력.html", context) """