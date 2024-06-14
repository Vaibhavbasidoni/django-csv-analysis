import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from .forms import UploadFileForm
import os
from django.conf import settings

def handle_uploaded_file(f):
    with open('temp.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            df = pd.read_csv('temp.csv')
            data_head = df.head().to_html()  # Convert DataFrame to HTML
            summary_stats = df.describe().to_html()  # Convert DataFrame to HTML
            missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()  # Convert Series to DataFrame to HTML

            # Create the directory if it doesn't exist
            static_dir = os.path.join(settings.BASE_DIR, 'static')
            os.makedirs(static_dir, exist_ok=True)

            histograms = []  # Store paths of generated histograms
            for column in df.select_dtypes(include='number').columns:
                plt.figure()
                sns.histplot(df[column].dropna(), kde=True)  # Using seaborn for histogram with KDE
                plt.title(f'Histogram for {column}')
                hist_path = os.path.join(static_dir, f'{column}.png')
                plt.savefig(hist_path)
                plt.close()
                histograms.append(os.path.join(settings.STATIC_URL, f'{column}.png'))  # Store relative path for the template

            return render(request, 'data_processor/results.html', {
                'data_head': data_head,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'histograms': histograms
            })
    else:
        form = UploadFileForm()
    return render(request, 'data_processor/upload.html', {'form': form})
