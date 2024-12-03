from django.shortcuts import render,redirect
from django.http import request
import pandas as pd
from django.contrib.auth.models import User as users
from datetime import datetime

def frc_data_entry(request):
    file_path = 'csv_path/excel_files/asset_register.xlsx'
    csv_file_path = 'csv_path/asset_info/asset_info.xlsx'
    df = pd.read_excel(file_path)
    df_csv = pd.read_excel(csv_file_path)

    # Extract values from the first column
    dropdown_categories = df_csv["Category"].tolist()

    if request.method == 'POST':
        file_path = 'csv_path/excel_files/asset_register.xlsx'
        df = pd.read_excel(file_path)
        
        # Extracting form data from the POST request
        purchase_date = request.POST.get('purchase_date')
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
        purchase_year = purchase_date.year
        purchase_month = purchase_date.month
        purchase_date = purchase_date.strftime('%m/%d/%Y')

        # Determine the financial year
        if purchase_month <= 6:
            purchase_year -= 1

        financial_year = f"{purchase_year}-{purchase_year + 1}"

        # Extract remaining form data
        serial_no = request.POST.get('serial_no')
        bill_no = request.POST.get('bill_no')
        category = request.POST.get('category')
        name_of_item = request.POST.get('name_of_item')
        quantity = float(request.POST.get('quantity') or 0)
        price = float(request.POST.get('price') or 0)
        warranty = request.POST.get('warranty')
        vendor = request.POST.get('vendor')
        vendor_address = request.POST.get('vendor_address')
        vendor_contact = request.POST.get('vendor_contact')
        sold_units = 0  # Assuming no initial sold units
        location = request.POST.get('location')
        current_condition = request.POST.get('current_condition')
        user_name = request.POST.get('user_name')
        depreciation_method = request.POST.get("depreciation")

        # Get the matching row from the DataFrame based on the category
        matching_row = df_csv[df_csv['Category'] == category].iloc[0]

        # Extract values from the matching row
        economic_code = matching_row['Economic Code']
        expected_life = matching_row['Expected Life']

        # Create the new row dictionary
        new_row = {
            'Financial Year': financial_year,
            'Purchase date': purchase_date,
            'Sl': serial_no,
            'Bill no': bill_no,
            'Category': category,
            'Name of Item': name_of_item,
            'Units': quantity,
            'Price': price,
            'Warranty (months)': warranty,
            'Vendor': vendor,
            'Vendor Address': vendor_address,
            'Vendor Contact': vendor_contact,
            'Sold (unit)': sold_units,
            'Location': location,
            'Economic Code': economic_code,
            'Expected life': expected_life,
            'Entry By': user_name,
            'Current Condition': current_condition,
            "Depreciation Method": depreciation_method
        }

        # Create the new dataframe with the column names you need
        new_dataframe_column_names = [
            'Financial Year', 'Purchase date', 'Sl', 'Bill no', 'Economic Code',
            'Category', 'Name of Item', 'Brand Name', 'Model/Type', 'Units',
            'Modified Number', 'Price', 'Salvage Value', 'Sold (unit)', "Vendor",
            "Vendor Address", "Vendor Contact", 'Sales proceeds', 'Years used(sold items)',
            'FY of Items sold', 'Cost of Assets Sold', 'Current Balance', 'Expected life',
            'Depreciation Method', 'Location', 'Status'
        ]

        # Check if the columns in the new row match the DataFrame
        columns_to_be_added = []
        for column in new_dataframe_column_names:
            if column not in df.columns.tolist():
                columns_to_be_added.append(column)

        # If there are columns missing, add them with default values (0 or None)
        for column in columns_to_be_added:
            df[column] = None  # Or 0, depending on the data type you expect

        # Convert new_row to a DataFrame
        new_row_df = pd.DataFrame([new_row], columns=new_dataframe_column_names)

        # Concatenate the new row with the existing DataFrame
        df = pd.concat([df, new_row_df], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df.to_excel(file_path, index=False)

        # Return the updated page or another view
        return render(request, 'frc_data_entry.html', {'dropdown_categories': dropdown_categories})

    return render(request, 'frc_data_entry.html', {'dropdown_categories': dropdown_categories})
