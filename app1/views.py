from django.shortcuts import render
import requests
import os
import multiprocessing

# Create your views here.



#Apply -n for windows to linux, -c for linux to linux.
def ping_server(ip):
    response = os.system(f"ping -n 1 {ip}")  
    if response == 0:
        return 'Reachable'
    else:
        return 'Not Reachable'


def server_list(request):
    if request.method == 'POST':
        server_list = request.POST.get('server_list')
        if server_list:    
            values = server_list.split()
            multiprocessing.freeze_support()
            pool = multiprocessing.Pool(processes=1)
            values  = pool.map(ping_server, values)  
            print("---------",values)
            server_status = [{'server_name': value, 'server_status': ping_server(value)} for value in values]

        return render(request, 'server_list.html', {'server_status': server_status})
    return render(request, 'server_list.html')
