import csv
from datetime import date
import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from afar_app.models import input_field
from assetinfo.models import model_asset_info
import pandas as pd
import numpy as np
from datetime import datetime
import re
import os
from django.conf import settings
from django.contrib import messages

file_path="csv_path/excel_files/asset_register.xlsx"

def frc_system(request):
    if request.method == 'POST':
        # Assuming your form field name is 'file'
        uploaded_file = request.FILES.get('file')

        if uploaded_file:
            # Read the existing Excel file
            existing_file_path = 'csv_path/excel_files/asset_register.xlsx'
            existing_df = pd.read_excel(existing_file_path)

            # Read the uploaded Excel file
            uploaded_df = pd.read_excel(uploaded_file)
            file=uploaded_df
            # Write the concatenated DataFrame to a new Excel file
            file_path = 'csv_path/excel_files/asset_register.xlsx'
            file.to_excel(file_path, index=False)
            return redirect('frc_asset_register')  # Redirect to appropriate view after upload

    return render(request, 'frc_system.html') 


def merge_files(request):
    if request.method == 'POST':
        # Assuming your form field name is 'file_to_merge'
        uploaded_file = request.FILES.get('file_to_merge')

        if uploaded_file:
            # Read the existing Excel file
            existing_file_path = 'csv_path/excel_files/asset_register.xlsx'
            existing_df = pd.read_excel(existing_file_path)

            # Read the uploaded Excel file
            uploaded_df = pd.read_excel(uploaded_file)

            # Concatenate the uploaded DataFrame with the existing DataFrame
            merged_df = pd.concat([existing_df, uploaded_df.iloc[1:]], ignore_index=True)

            # Write the merged DataFrame to the existing Excel file
            file_path = 'csv_path/excel_files/asset_register.xlsx'
            merged_df.to_excel(file_path, index=False)

            return redirect('frc_asset_register')  # Redirect to appropriate view after merge

    return render(request, 'frc_system') 

def format_maker():
    df=pd.read_excel(file_path)
    df.head(0).to_excel("csv_path/excel_files/asset_register_format.xlsx",index=False)
    return None


def download_format(request):
    format_maker()
    try: 
        file_path = os.path.join(settings.BASE_DIR, 'csv_path/excel_files/asset_register_format.xlsx')

        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=asset_register_format.xlsx'
            return response

    except:
        return HttpResponse("No file Exists")  