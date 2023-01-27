# app
from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
# Create your views here.


# view function that will handle the webhook from Flutterwave
def handle_webhook(request):
    # request method is POST
    if request.method == 'POST':
        # Getting the JSON data from the request body
        data = json.loads(request.body)
        
        # Extract the necessary information from the webhook data
        transaction_id = data.get('tx.id')
        amount = data.get('tx.amount')
        email = data.get('customer.email')
        service_purchased = data.get('meta.service')

        # Use the transaction_id to retrieve more information from the Flutterwave API
        headers = {'Authorization': 'Bearer YOUR_SECRET_KEY'}
        url = f'https://api.flutterwave.com/transactions/{transaction_id}'
        response = requests.get(url, headers=headers)
        transaction_data = response.json()
        
        # Extract the necessary information from the API response
        name = transaction_data.get('customer.name')
        phone = transaction_data.get('customer.phone')

        # Log the information for debugging
        print(f'Name: {name}, Email: {email}, Phone: {phone}, Amount: {amount}, Service Purchased: {service_purchased}')
        
        # Send an email to the service provider and the customer using the mailerlite-api-v2-node
        # Code to send an email goes here
        
        # Return a JSON response to acknowledge receipt of the webhook
        return JsonResponse({'status': 'success'})
    else:
        # Return a JSON response indicating that the request method is invalid
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
