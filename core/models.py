from django.db import models

import core.zoom_api as zoom_api


class ZoomMeeting(models.Model):
    meeting_id = models.IntegerField(unique=True)
    nb_of_participants = models.IntegerField(default=0)

    def to_json(self):
        return {self.meeting_id: self.nb_of_participants}

    def update_number_of_participants(self):
        nb_of_participants = zoom_api.get_number_of_participants(self.meeting_id)
        if nb_of_participants == -1:
            self.delete()
            return
        self.nb_of_participants = nb_of_participants
        self.save(update_fields=["nb_of_participants"])

    def interrupt_meeting(self):
        zoom_api.interrupt_meeting(self.meeting_id)
        self.delete()

    @classmethod
    def get_meetings_from_zoom_api(cls):
        meetings = zoom_api.get_meetings()
        list_zoom_meeting = []
        for meeting_id in meetings:
            list_zoom_meeting.append(cls(meeting_id=meeting_id))
        cls.objects.bulk_create(list_zoom_meeting, ignore_conflicts=True)
