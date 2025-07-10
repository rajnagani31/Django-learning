from django.shortcuts import render
from query_set.models import Student, Teacher
from django.db.models import Q

# Create your views here.


#  Q query set mean ~(not), &(AND), |(or)
def Q_set(request):

    data = Student.objects.all().order_by("id")
    # all_data=data.filter(Q(id=4) & Q(roll_num=105))
    # all_data=data.filter(Q(id=45) | Q(roll_num=191))

    # all_data=data.filter(~Q(id=75))

    # all_data=data.filter(Q(id__in=[1,3,4]) & Q(marks__lte=100))
    # all_data=data.filter(Q(city='pune') & Q(marks=150))
    all_data = data.filter(
        Q(city="surat") | Q(city="pune") | Q(city="rajkot"), marks__in=[100, 0, 50, 150]
    )

    data_limit = Student.objects.all().order_by("id")
    all_data = data_limit[0:20]
    all_data = data_limit[5:50:-1]

    all_data = Student.objects.create(
        name="krishna", roll_num=200, city="rajkot", marks=50, passing_year="2024-06-16"
    )

    all_data, create = Student.objects.get_or_create(
        name="bhalani prince",
        roll_num=200,
        city="bangloru",
        marks=10,
        passing_year="2026-06-16",
    )

    # bulk update

    object_to_data = [
        Student(id=154, name="omm", marks=500),
        Student(id=155, name="smit", marks=70, passing_year="2022-7-13"),
        Student(id=156, name="dive", marks=150, passing_year="2024-8-9"),
        Student(id=157, name="omik", marks=80, passing_year="2021-3-21"),
    ]

    data = Student.objects.all()

    for i in data:
        if i.marks == 10:

            print(i)

    # all_data=Student.objects.bulk_update(data,['marks'])
    all_data = Student.objects.filter(marks=10).delete()

    all_data = Student.objects.create(
        name="krishna", roll_num=200, city="rajkot", marks=50, passing_year="2024-06-16"
    )

    # all_data,create=Student.objects.get_or_create(name='bhalani prince' , roll_num=200 , city='bangloru' ,marks=10,passing_year='2026-06-16')

    all_data = Student.objects.in_bulk([216, 217])
    print(all_data)

    print("yes")
    return render(request, "q/q.html", {"table": all_data})
