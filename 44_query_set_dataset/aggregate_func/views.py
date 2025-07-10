from django.shortcuts import render
from query_set.models import Student, Teacher
from django.db.models import Sum, Avg, Min, Max, Count


# Create your views here.
def home(request):

    student_all_data = Student.objects.all()

    sum = student_all_data.aggregate(Sum("marks"))
    avg = student_all_data.aggregate(Avg("marks"))
    min = student_all_data.aggregate(Min("marks"))
    max = student_all_data.aggregate(Max("marks"))
    count_id = student_all_data.aggregate(Count("id"))
    count_0 = student_all_data.filter(marks=0).aggregate(Count("marks"))
    count_100 = student_all_data.filter(marks=100).aggregate(Count("marks"))
    count_150 = student_all_data.filter(marks=150).aggregate(Count("marks"))

    surat = student_all_data.filter(city="surat").aggregate(Count("city"))
    pune = student_all_data.filter(city="pune").aggregate(Count("city"))
    all_data = Student.objects.all().order_by("id").values().filter()

    count_2023 = student_all_data.filter(passing_year__year=2023).aggregate(
        Count("passing_year")
    )
    count_2024 = student_all_data.filter(passing_year__year=2024).aggregate(
        Count("passing_year")
    )
    count_2025 = student_all_data.filter(passing_year__year=2025).aggregate(
        Count("passing_year")
    )
    count_2026 = student_all_data.filter(passing_year__year=2026).aggregate(
        Count("passing_year")
    )

    all_data = Student.objects.all()
    # data=Student.objects.filter(id__in=[63,64,65,69,70,101,103,93,56,78])
    # all_data=data.filter(marks=0).update(marks=100)

    for data in all_data:
        if data.pk % 2 == 0:
            if data.city == "pune":
                data.city = "surat"
    all_data = Student.objects.bulk_update(all_data, ["city"])
    aggregate_data = {
        "sum": sum,
        "avg": avg,
        "min": min,
        "max": max,
        "count_id": count_id,
        "marks_0": count_0,
        "marks_100": count_100,
        "marks_150": count_150,
        "surat": surat,
        "pune": pune,
        "2023": count_2023,
        "2024": count_2024,
        "2025": count_2025,
        "2026": count_2026,
    }
    return render(
        request, "aggr/aggregate.html", {"table": all_data, "data": aggregate_data}
    )
