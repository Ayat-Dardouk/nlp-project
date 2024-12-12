from django.shortcuts import render
from django.http import HttpResponse
from .services.parse_resume import extract_text_from_pdf, parse_resume, save_to_excel
from django.core.files.storage import FileSystemStorage

import warnings
warnings.filterwarnings("ignore", category=FutureWarning, message=".*register_pytree_node.*")


def upload_resume(request):
    if request.method == 'POST' and request.FILES['resume']:
        resume_file = request.FILES['resume']  # Get the uploaded file
        
        # Extract text from the PDF file
        resume_text = extract_text_from_pdf(resume_file)
        
        # Parse the resume text
        parsed_data = parse_resume(resume_text)
        
        # Save parsed data to Excel and send to the user
        file_name = save_to_excel(parsed_data)
        
        # Return the Excel file as a download
        response = HttpResponse(
            content=open(file_name, 'rb').read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response
    return render(request, 'upload.html')

        
 
