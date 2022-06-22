from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from crud.models import tbl_student
from django.contrib import messages

# Create your views here.


def index(request):
    context = {"demoVar": "Sent using Variable"}
    request.session['fav_color'] = context['demoVar']
    return render(request, "index.html", context)
    # return HttpResponse("Lisitng of Students")


def create(request, id=""):
    if request.method == "POST":
        if request.POST.get("id") != "":
            name = request.POST.get("name")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            city = request.POST.get("city")
            address = request.POST.get("address")

            student = tbl_student.objects.get(id=id)

            student.name = name
            student.email = email
            student.mobile = mobile
            student.city = city
            student.address = address
            student.save()
            messages.success(request, "Student updated successfully.")
            return redirect("/all")

        else:
            name = request.POST.get("name")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            city = request.POST.get("city")
            address = request.POST.get("address")
            created_on = datetime.today()

            student = tbl_student(
                name=name,
                email=email,
                mobile=mobile,
                city=city,
                address=address,
                created_on=created_on,
            )
            student.save()
            messages.success(request, "Student added successfully.")
            return redirect("/all")

    if id != "":
        context = {"single_student": tbl_student.objects.get(id=id), "id": id}
        return render(request, "create.html", context)

    return render(request, "create.html")


def edit(request, id):
    return HttpResponse("Edit Students " + str(id))


def about(request):
    context = {
        'session_data': request.session['fav_color']
    }
    return render(request, "about.html", context)


def getall(request):
    context = {"student": tbl_student.objects.all()}
    return render(request, "display.html", context)

def delete(request, id=""):
    if id != '':
        tbl_student.objects.filter(id=id).delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("/all")