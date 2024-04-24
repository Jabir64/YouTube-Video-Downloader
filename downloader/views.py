from django.shortcuts import render,redirect
from pytube import YouTube
from .forms import VideoForm

def download_video(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        video_url = form.cleaned_data['url']
        yt = YouTube(video_url)
        title = yt.title
        stream = yt.streams.get_highest_resolution()
        stream.download()
        form.save()
        return render(request, 'success.html', {'title': title})
    return render(request, 'download.html', {'form': form})
