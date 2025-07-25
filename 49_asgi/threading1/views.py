from django.http import JsonResponse
from django.shortcuts import render
import threading,time
# Create your views here.
def start_thread(request):
    start_time=time.time()
    def user():
        for i in range(1,5):
            time.sleep(5)
            print(f"Student {i} ")

    def account():
        for i in range(1,5):
            time.sleep(2)
            print(f"profile are created")

    user_thread=threading.Thread(target=user)
    account_thread=threading.Thread(target=account)

    user_thread.start()
    account_thread.start()

    user_thread.join()
    account_thread.join()
           
    end_time=time.time()
    time_taken=end_time-start_time
    print("process are competed")
    return JsonResponse({
        "data":'student',
        "Time": time_taken
    })
         