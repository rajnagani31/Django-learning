from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from query_set.models import Student, Teacher
from django.template import loader
from django.http import HttpResponse
from datetime import date


# Create your views here.
def home(request):

    all_data = Student.objects.get(id=2)

    all_data = [Student.objects.first()]

    all_data = Student.objects.all()
    all_data = [Student.objects.get(pk=3)]

    all_data = Student.objects.filter(name="krish")
    all_data = Student.objects.values("id", "name")

    all_data = Student.objects.all()
    print(all_data.exists())

    # all_data=Student.objects.filter(name='vidr')
    # print(all_data.exists())

    data = Student.objects.get(pk=5)
    print(all_data.filter(pk=data.pk).exists())

    data = Student.objects.all()
    all_data = data.filter(name__iexact="vidr")

    all_data = str(data.count())
    print(all_data)

    # create
    all_data = Student.objects.create(
        name="rahul",
        roll_num="15",
        city="gandhinger",
        marks=100,
        passing_year="2023-6-4",
    )

    # get_or_creat
    all_data, created = Student.objects.get_or_create(
        name="prince", roll_num="16", city="rajkot", marks=100, passing_year="2023-6-4"
    )
    print(created)

    # Singul data Update
    all_data = Student.objects.filter(marks="100").update(
        name="bhalani prince", city="rajkot"
    )

    # update_or_create
    # bulk data create

    objs = [
        Student(
            name="ruchi",
            roll_num="189",
            city="surat",
            marks="100",
            passing_year="2024-08-12",
        ),
        Student(
            name="parth",
            roll_num="190",
            city="surat",
            marks="100",
            passing_year="2024-07-12",
        ),
        Student(
            name="darshan",
            roll_num="191",
            city="surat",
            marks="100",
            passing_year="2024-06-5",
        ),
    ]
    all_data = Student.objects.bulk_create(objs)

    # bulk update
    all_data = Student.objects.all()
    for data in all_data:
        data.marks = 0
    all_data = Student.objects.bulk_update(all_data, ["marks"])

    # in_bulk retrive data in dict(key value peaurs)
    all_data = Student.objects.in_bulk([1])

    # all_data=Student.objects.get(pk=40).delete()
    all_data = Student.objects.filter(city="surat").delete()

    #  print sql query
    print("all data query:", all_data)
    print(all_data)
    print(f"Type:{type(all_data)}")

    return render(request, "query_set/query.html", {"table": all_data})
    # return HttpResponse(template.render(context,request))
