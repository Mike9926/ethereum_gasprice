# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import GasPrice
#import my script
from django.core.management import call_command # Import the call_command functi


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
    return render(request, "gasprice/home.html", context)
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
def gas_price_detail(request, pk):
    # Get the gas price object from the database
    gas_price = GasPrice.objects.get(pk=pk)
    # Create a context dictionary with the gas price data
    context = {
        "gas_price": gas_price
    }
    # Return a render function call with the request, the template name, and the contexts
    return render(request, "gasprice/gas_price_detail.html", context)
