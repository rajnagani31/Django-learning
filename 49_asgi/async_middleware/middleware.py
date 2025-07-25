from asgiref.sync import iscoroutinefunction,markcoroutinefunction
from django.utils.decorators import sync_and_async_middleware,async_only_middleware,sync_only_middleware # use in function base middleware

# sync middleware

class syncMiddleware():
    def __init__(self,get_response):
        async_capable=False
        sync_capable=True
        self.get_response = get_response
        print(" one time ")

    def __call__(self, request):
        print(f" Before view (sync): {request.path}")
        response=self.get_response(request)
        print(f'"After view (sync) : {request.path}') 
        return response
    
# Async middleware 

class AsyncMiddleware():
        async_capable = True
        sync_capable = False

        def __init__(self,get_response):
            self.get_response = get_response
            if iscoroutinefunction(self.get_response):
                markcoroutinefunction(self)

            print("one time")

        async def __call__(self,request):
            print (f"Run befor view (async):{request.path}")
            response= await self.get_response(request)
            print(f"Run after view (Async): {request.path}")
            return response    