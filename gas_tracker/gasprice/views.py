# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import GasPrice
#import my script
from django.core.management import call_command # Import the call_command functi
from .management.commands.fetch_gas_prices import Command


# Home view
def home(request):
# Try to run your command
    try:
        # Call your command with the option --schema=schema_name
        call_command("fetch_gas_prices", schema="schema_name")
        # Print a success message
        print("Command executed successfully")
    except Exception as e:
        # Handle any errors or exceptions
        print(f"Command failed. Error: {e}")

    # Get the latest gas price object from the database
    latest_gas_price = GasPrice.objects.latest("timestamp")
    # Get all the gas price objects from the database
    gas_prices = GasPrice.objects.all()
    # Create a context dictionary with the gas price data
    context = {
        "latest_gas_price": latest_gas_price,
        "gas_prices": gas_prices
    }
    # Return a render function call with the request, the template name, and the contexts
    return render(request, "gasprice/index.html", context)

def fetch_gas_prices(request):
    # Run your script to fetch and store gas prices
    fetch_gas_prices()
    # Get the latest gas price object from the database
    latest_gas_price = GasPrice.objects.latest("timestamp")
    # Create a dictionary with the gas price data
    data = {
        "gas_price": latest_gas_price.gas_price,
        "transaction_speed": latest_gas_price.transaction_speed,
        "timestamp": latest_gas_price.timestamp
    }
    # Return a JSON response with the data
    return JsonResponse(data)


# About view
def about(request):
    # Return a render function call with the request and the template names
    return render(request, "gasprice/about.html")

# Contact view
def contact(request):
    # Return a render function call with the request and the template name
    return render(request, "gasprice/contact.html")

# Gas price detail view
def gas_price_detail(request, id):
    # Get the gas price object that matches the id or raise a 404 error if not found
    gas_price = get_object_or_404(GasPrice, id=id)
    # Render the template with the gas price object as context
    return render(request, 'gasprice/gas_price_detail.html', {'gas_price': gas_price})

def update_gas_price(request):
    command = Command()
    command.handle()
    latest_gas_price = GasPrice.objects.latest('timestamp')
    data = {
        'gas_price': latest_gas_price.gas_price,
        'transaction_speed': latest_gas_price.transaction_speed,
        'timestamp': latest_gas_price.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return JsonResponse(data)
