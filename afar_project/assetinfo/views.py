from django.shortcuts import render
from .models import model_asset_info
import pandas as pd
file_path="csv_path/asset_info/asset_info.xlsx"
# Create your views here.
def asset_info(request):
    if request.method == "POST":
        category = request.POST.get('category')
        code = request.POST.get('code')
        economicCode = request.POST.get('economicCode')
        expectedLife = request.POST.get('expectedLife')
        depreciationMethod = request.POST.get('depreciationMethod')
        asset_form_inputs_loop = []
        for field_name, field_value in request.POST.items():
            if field_name != 'csrfmiddlewaretoken':
                asset_form_inputs_loop.append(field_value)

        asset_input_field = model_asset_info(category=category, code=code,economic_code = economicCode,expected_life = expectedLife,depreciation_method = depreciationMethod)
        asset_input_field.save()

        
        csv_file_path = 'csv_path/asset_info/asset_info.xlsx'
        
        # Read existing CSV file into DataFrame
        df = pd.read_excel(csv_file_path)
        
        # Create a new DataFrame with user input as a row
        new_row = pd.DataFrame([asset_form_inputs_loop], columns=df.columns)
        
        # Concatenate the existing DataFrame with the new row
        df = pd.concat([df, new_row], ignore_index=True)
        
        # Write the updated DataFrame to the CSV file
        df.to_excel(csv_file_path, index=False)

    return render(request, "asset_info.html")
def current_asset_info(request):
    df = pd.read_excel('csv_path/asset_info/asset_info.xlsx')

    header = df.columns.tolist()
    rows = df.values.tolist()

    return render(request, "current_asset_info.html",{'header': header, 'rows': rows})

def upload_files_to_asset_info(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        
        # Read the uploaded CSV file
        df_uploaded = pd.read_csv(uploaded_file,encoding="utf-8-sig")
        
        # Merge with another file (assuming 'another_file.csv' exists)
        
        # Save the merged DataFrame as df_another.csv
        df_uploaded.to_csv(file_path, index=False)
        return 0




