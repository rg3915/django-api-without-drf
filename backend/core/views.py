import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import VideoForm
from .models import Video


@require_http_methods(['GET'])
def video_list(request):
    videos = Video.objects.all()
    data = [video.to_dict() for video in videos]
    return JsonResponse({'data': data})


@require_http_methods(['GET'])
def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    data = video.to_dict()
    return JsonResponse({'data': data})


@csrf_exempt
@require_http_methods(['POST'])
def video_create(request):
    form = VideoForm(request.POST or None)

    if request.POST:
        # Dados obtidos pelo formulário.
        if form.is_valid():
            video = form.save()

    elif request.body:
        # Dados obtidos via json.
        data = json.loads(request.body)
        video = Video.objects.create(**data)

    else:
        return JsonResponse({'message': 'Algo deu errado.'})

    return JsonResponse({'data': video.to_dict()})


@csrf_exempt
@require_http_methods(['POST'])  # Não aceita PUT
def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST or None, instance=video)

    if request.POST:
        # Dados obtidos pelo formulário.
        if form.is_valid():
            video = form.save()

    elif request.body:
        # Dados obtidos via json.
        data = json.loads(request.body)

        for attr, value in data.items():
            setattr(video, attr, value)
        video.save()

    else:
        return JsonResponse({'message': 'Algo deu errado.'})

    return JsonResponse({'data': video.to_dict()})


@csrf_exempt
@require_http_methods(['DELETE'])
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    return JsonResponse({'data': 'Item deletado com sucesso.'})


@csrf_exempt
def videos(request):
    videos = Video.objects.all()
    data = [video.to_dict() for video in videos]
    form = VideoForm(request.POST or None)

    if request.method == 'POST':
        if request.POST:
            # Dados obtidos pelo formulário.
            if form.is_valid():
                video = form.save()

        elif request.body:
            # Dados obtidos via json.
            data = json.loads(request.body)
            video = Video.objects.create(**data)

        else:
            return JsonResponse({'message': 'Algo deu errado.'})

        return JsonResponse({'data': video.to_dict()})

    return JsonResponse({'data': data})


@csrf_exempt
def video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST or None, instance=video)

    if request.method == 'GET':
        data = video.to_dict()
        return JsonResponse({'data': data})

    if request.method == 'POST':
        if request.POST:
            # Dados obtidos pelo formulário.
            if form.is_valid():
                video = form.save()

        elif request.body:
            # Dados obtidos via json.
            data = json.loads(request.body)

            for attr, value in data.items():
                setattr(video, attr, value)
            video.save()

        else:
            return JsonResponse({'message': 'Algo deu errado.'})

        return JsonResponse({'data': video.to_dict()})

    if request.method == 'DELETE':
        video.delete()
        return JsonResponse({'data': 'Item deletado com sucesso.'})
