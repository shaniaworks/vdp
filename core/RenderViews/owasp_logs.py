from django.shortcuts import render


#Getting owasp log file functions

def get_logs(request):
    if request.method == "POST":
        data = {}
        print("Where is the data")
        return render(request,'owasp.html',data)