from django.shortcuts import HttpResponse, render


# function base middleware
def my_fun(get_response):
    print("It's working")  # write one time code ex configer,any cheaking etc

    def my_middleware(request):
        print("Before view")
        # response = get_response(request) # ------------> run view
        # response=HttpResponse('Site is under ') #-------------> run httpresponse
        response = render(
            request, "app1/site.html"
        )  # ----------------->template basd middleware

        print("After view")
        return response

    return my_middleware


# class base middleware
class myClmiddle:
    def __init__(self, get_response):
        self.get_response = get_response
        print("It work on one time")

    def __call__(self, request):
        print("Befor view")
        response = self.get_response(request)
        # response=render(self,request,'app1/site.html')
        print("After view")
        return response


# Process_view middleware
class myProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        # use case ----> run code before view(like user chekaing ,templet render ,http response etc)
        print("Many use case befor finel view")

        return None

    # Exception middlewares

    class myExceptionMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            response = self.get_response(request)
            return response

        def process_exception(self, request, exception):
            print("run exception")
            msg = exception
            class_name = exception.__class__.__name__
            print(class_name)
            print(msg)
            return HttpResponse(msg)


# process templates middleware


class MyTemplatesMiddleware:
    print("Template middleware")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        # name=input("Enter a username:")
        print("Process template middleware work")
        response.context_data["name"] = "manush"
        return response
