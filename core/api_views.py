from django.http import JsonResponse

from core.models import ZoomMeeting


def get_meetings(request):
    """
    The view get meetings either from db (possibly stale data) or from the zoom API
    the behavior is controlled through the request parameter 'refresh'.

    :param request:
    :return:
    """
    response = []
    if request.GET.get("refresh") == "true":
        return update_all_meetings(request)

    else:
        for zoom_meeting in ZoomMeeting.objects.all():
            response.append(zoom_meeting.to_json())

    return JsonResponse(response, status=200, safe=False)


def update_meeting(request, meeting_id):
    try:
        zoom_meeting = ZoomMeeting.objects.get(meeting_id=meeting_id)
    except (ZoomMeeting.DoesNotExist, ValueError) as e:
        return JsonResponse(e, status=404, safe=False)

    zoom_meeting.update_number_of_participants()

    return JsonResponse(zoom_meeting.to_json(), status=200)


def interrupt_meeting(request, meeting_id):
    try:
        zoom_meeting = ZoomMeeting.objects.get(meeting_id=meeting_id)
    except ZoomMeeting.DoesNotExist:
        return JsonResponse({}, status=404)
    try:
        zoom_meeting.interrupt_meeting()
    except ValueError:
        return JsonResponse({}, status=400)

    return JsonResponse(zoom_meeting.to_json(), status=200)


def update_all_meetings(request):
    try:
        ZoomMeeting.get_meetings_from_zoom_api()
    except ValueError:
        return JsonResponse({}, status=400)

    response = {}
    for zoom_meeting in ZoomMeeting.objects.all():
        zoom_meeting.update_number_of_participants()
        response = {**response, **zoom_meeting.to_json()}

    return JsonResponse(response, status=200, safe=False)
