from django.shortcuts import redirect, render
from django.http import HttpResponse

#Getting owasp log file functions

def get_logs(request):
    data = {}
    if request.method == "POST":
        file_name = request.POST.get("file_name")
        file = request.POST.get("file")
        print(file)
        print(file_name)

        from core.scanner import main
        
        main()

        return redirect('/')
    return render(request,'owasp.html',data)