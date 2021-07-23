import requests

from jenniferclinic.settings import ZOOM_TOKEN

headers = {
    'Authorization': f"Bearer {ZOOM_TOKEN}",
    'Content-Type': "application/json"
}

BASE_URL = "https://api.zoom.us/v2"


def get_number_of_participants(meeting_id):
    """
    Call zoom API to get number of participants, if room is not found in zoom returns -1
    :param meeting_id:
    :return:
    """
    nb_participants = 0
    response = requests.get(f"{BASE_URL}/metrics/meetings/{meeting_id}/participants", headers=headers)
    status_code = response.status_code
    if status_code == 404:
        return -1
    if status_code != 200:
        raise ValueError
    participants = response.json()["participants"]
    for participant in participants:
        if "leave_time" not in participant and "leave_reason" not in participant:
            nb_participants += 1

    return nb_participants


def get_meetings():
    response = requests.get(f"{BASE_URL}/metrics/meetings", headers=headers)
    if response.status_code != 200:
        raise ValueError
    meetings = response.json()["meetings"]
    return [meeting["id"] for meeting in meetings]


def interrupt_meeting(meeting_id):
    response = requests.put(f"{BASE_URL}/meetings/{meeting_id}/status", headers=headers, json={
        "action": "end"
    })
    if response.status_code != 204:
        raise ValueError
