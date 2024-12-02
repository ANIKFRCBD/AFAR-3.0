from django.shortcuts import render
from django.http import HttpResponseBadRequest
import pandas as pd
from PIL import Image as PILImage
import os

def asset_image_upload(request):
    file_path = 'csv_path/excel_files/asset_register.xlsx'  
    df_sheet = pd.read_excel(file_path)
    df = df_sheet
    asset_code_options = df["Asset Code"].tolist()

    if request.method == 'POST':
        dropdown_option = request.POST.get('dropdown_asset_code')
        uploaded_image = request.FILES.get('image')

        if not dropdown_option:
            return HttpResponseBadRequest("dropdown_asset_code not found in the request.")
        
        if not uploaded_image:
            return HttpResponseBadRequest("No image file uploaded.")

        try:
            image = PILImage.open(uploaded_image)
            save_path = os.path.join('static', "asset_images", dropdown_option + '.jpg')
            image.save(save_path, 'JPEG')

            # Optionally, you can save the image path in your database
            # For example, if you have a model named Image:
            # Image.objects.create(name=dropdown_option, path=save_path)

        except Exception as e:
            return HttpResponseBadRequest(f"Error saving image: {e}")

    return render(request, 'asset_image_upload.html', {'asset_code_options': asset_code_options})
