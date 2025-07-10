from django.shortcuts import render
from .models import Student, Teacher
from django.template import loader
from django.http import HttpResponse
from datetime import date


# Create your views here.
def home_table(request):
    all_data = Student.objects.all()

    # filter
    all_data = Student.objects.filter(city="surat")  # ---> filter use specific field

    # exclude
    all_data = Student.objects.exclude(
        city="surat"
    )  # ---> exclude use in this field nott show other field show

    # order_by '-' big to small rendmli data use '?' ,fix data show use [0:5:2]
    all_data = Student.objects.order_by("marks")
    all_data = Student.objects.order_by("?")
    all_data = Student.objects.order_by("id")[0:5]

    # only show specific value ex id,name,rol and data show in tuple use values_list
    all_data = Student.objects.values("id", "name", "city", "roll_num")
    all_data = Student.objects.values_list("id", "name")

    # use sets union,intersection,and,or
    # union
    qs1 = Student.objects.values_list("name", named=True)
    qs2 = Teacher.objects.values_list("name", named=True)
    all_data = qs2.union(qs1)

    # intersection
    all_data = qs2.intersection(qs1)

    all_data = Student.objects.all().values()

    all_data = Student.objects.all().values("id").filter(name="raj")

    # exact give all datelis according mu need ,they give same to same value
    all_data = Student.objects.filter(name__exact="vidr")

    # iexact give sam char are match the value send to user raj,Raj both value is right
    all_data = Student.objects.filter(name__iexact="Raj")

    # contains='r' accourding perameter return with all matching records
    all_data = Student.objects.filter(name__contains="r")

    all_data = Student.objects.filter(name__icontains="v")

    all_data = Student.objects.values("id", "name")

    # specific id and slicing with id
    all_data = Student.objects.filter(id__in=[1, 2, 3, 4, 5][0:10:2])

    # gt(>),lt(<),gte(<=),lte(>=)
    all_data = Student.objects.filter(marks__gt=100)
    all_data = Student.objects.filter(marks__gte=100)
    all_data = Student.objects.filter(marks__lt=100)
    all_data = Student.objects.filter(marks__lte=100)

    # and leater to start data and start leater to start data is avalibale

    # data commpare usin date
    all_data = Student.objects.filter(passing_year__range=("2023-01-01", "2023-6-30"))
    # all_data=Student.objects.filter(passing_year__date=date(2023,1,1))

    # specific year details wit <,>
    all_data = Student.objects.filter(passing_year__year__lt=2025)
    all_data = Student.objects.filter(passing_year__year__gt=2020)
    all_data = Student.objects.filter(passing_year__year=2025)

    # specific month use <,> (__month__gt=3) and day,week,month, lookups is available
    all_data = Student.objects.filter(passing_year__month__lt=3)
    all_data = Student.objects.filter(passing_year__month=3)

    all_data = Student.objects.filter(id__in=[1, 2, 3, 4, 5])
    all_data = Student.objects.values("name").filter(name__in=["raj", "vidr"])

    all_data = Student.objects.filter(passing_year__year=2025)
    all_data = Student.objects.all()

    # other database queryset method

    all_data = [Student.objects.get(id=2)]

    all_data = [Student.objects.first()]

    template = loader.get_template("query_set/query.html")

    context = {"table": all_data}
    #  print sql query
    print("all data query:", all_data)
    print(all_data)
    print(f"Type:{type(all_data)}")

    return render(request, "query_set/query.html", {"table": all_data})
    # return HttpResponse(template.render(context,request))
