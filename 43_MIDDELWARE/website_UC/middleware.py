from django.shortcuts import render
from .models import underConstruction

# from  decouple  import config
# from dotenv import load_dotenv


# load_dotenv()
class UnderCoustructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # is staff is true admin show website but user not show
        if request.user.is_staff:
            return self.get_response(request)

        uc_key = "123"
        if "u" in request.GET and request.GET["u"] == uc_key:
            return self.get_response(request)

        try:
            uc = underConstruction.objects.first()

            if uc and uc.is_under_construction:
                context = {"note": uc.Uc_note, "duration": uc.uc_duration}
                return render(request, "website_UC/uc.html", context)

        except:
            pass
        return self.get_response(request)
