from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection

def home(req):
	return render(req,'index.html')

def receive_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        if message.lower() == 'admin details':
            # Fetch admin details from the database
            with connection.cursor() as cursor:
                cursor.execute("SELECT username, password FROM admin")  # Change the table name and id as needed
                admin_data = cursor.fetchone()

                if admin_data:
                    admin_username, admin_password = admin_data
                    response_message = f"{admin_username} , **{admin_password}**"
                else:
                    response_message = "Admin details not found"
        else:
            response_message = f"You said: {message}"

        return JsonResponse({'message': response_message})

    return JsonResponse({'error': 'Invalid request method'}, status=400)