from django.shortcuts import render, redirect
import requests
import json

def home_page(request):
    if request.method == 'POST':
        id_instance = request.POST.get('id_instance')
        api_token = request.POST.get('api_token')
        action = request.POST.get('action')

        if action == 'get_settings':
            request.session['id_instance'] = id_instance
            request.session['api_token'] = api_token
            return redirect('get_settings')

        elif action == 'get_state':
            request.session['id_instance'] = id_instance
            request.session['api_token'] = api_token
            return redirect('get_state')


    return render(request, 'index.html')



# ============================== getSettings ===================================

def get_settings(request):
    id_instance = request.session.get('id_instance')
    api_token = request.session.get('api_token')

    if not id_instance or not api_token:
        return redirect('home_settings')

    url_settings = f"https://api.green-api.com/waInstance{id_instance}/getSettings/{api_token}"
    settings_response = requests.get(url_settings, headers={})

    try:
        settings_data = settings_response.json()
    except json.JSONDecodeError as e:
        settings_data = {'error': f"Error decoding JSON: {e}"}

    return render(request, 'getSettings.html', {'settings_data': settings_data, 'state_data': None})

# ============================== getStateInstance ===================================

def get_state(request):
    id_instance = request.session.get('id_instance')
    api_token = request.session.get('api_token')

    if not id_instance or not api_token:
        return redirect('home_settings')

    url_state = f"https://api.green-api.com/waInstance{id_instance}/getStateInstance/{api_token}"
    state_response = requests.get(url_state, headers={})

    try:
        state_data = state_response.json()
    except json.JSONDecodeError as e:
        state_data = {'error': f"Error decoding JSON: {e}"}

    return render(request, 'getStateInstance.html', {'settings_data': None, 'state_data': state_data})


# ============================== Send Message ===================================

def send_message(request):
    id_instance = request.session.get('id_instance')
    api_token = request.session.get('api_token')

    if not id_instance or not api_token:
        return redirect('home_settings')

    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        message = request.POST.get('message')

        if chat_id and message:
            url = f"https://api.green-api.com/waInstance{id_instance}/sendMessage/{api_token}"
            payload = {
                "chatId": chat_id,
                "message": message
            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, headers=headers, json=payload)

            response_data = {
                'status': response.status_code,
                'message': response.text,
                'chat_id_sent': chat_id,
                'message_sent': message,
            }
        else:
            response_data = {'error': 'Please provide both chat ID and message'}

        return render(request, 'send_message.html', {'response_data': response_data})

    return render(request, 'send_message.html', {'response_data': None})



# ============================== getStateInstance ===================================

def send_file_by_url(request):
    id_instance = request.session.get('id_instance')
    api_token = request.session.get('api_token')

    if not id_instance or not api_token:
        return redirect('home_settings')

    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        file_url = request.POST.get('file_url')
        file_name = request.POST.get('file_name')
        caption = request.POST.get('caption')

        if chat_id and file_url and file_name:
            url = f"https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{api_token}"

            payload = {
                'chatId': chat_id,
                'urlFile': file_url,
                'fileName': file_name,
                'caption': caption
            }

            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, headers=headers, json=payload)

            response_data = {
                'status': response.status_code,
                'message': response.text,
                'chat_id_sent': chat_id,
                'file_url_sent': file_url,
                'file_name_sent': file_name,
                'file_caption_sent': caption
            }
        else:
            response_data = {'error': 'Please provide both chat ID and file URL'}

        return render(request, 'send_file_by_url.html', {'response_data': response_data})

    return render(request, 'send_file_by_url.html', {'response_data': None})



