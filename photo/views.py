from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo
from photo.forms import PhotoEditForm

def single_photo(request, photo_id, hidden=False):

	photo = get_object_or_404(Photo, pk=photo_id)

	response_text = '<p>{photo_id}번 사진을 보여드립니다.</p>'
	response_text += '<p>{photo_url}</p>'
	response_text += '<p><img src="{photo_url}"/></p>'

	response_text += '<p>{photo_filtered_url}</p>'
	response_text += '<p><img src ="{photo_filtered_url}"/></p>'


	return HttpResponse(response_text.format(photo_id = photo_id, photo_url = photo.image_file.url, photo_filtered_url = photo.filtered_image_file.url))

def new_photo(reqeust):
	edit_form = PhotoEditForm()

	return render(request, 'new_photo.html', {'form': edit_form,})
