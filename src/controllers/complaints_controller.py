from src.models.complaints_model import *
from src.models.responses_model import *

from src.views.complaints_list_view import *
from src.views.complaint_detail_view import *
from src.views.complaint_reply_view import *

class ComplaintsController:
    def index(self):
        rows = get_all_complaints()
        action = render_complaints_list(rows)

        if action[0] == "detail":
            return ("complaints.detail", action[1])
        return ("home", None)

    def detail(self, complaint_id: int):
        complaint = get_description_by_id(complaint_id)
        if not complaint:
            return ("complaints.index", None)

        responses = get_responses_by_complaint_id(complaint_id)

        action = render_complaint_detail(complaint, responses)

        if action[0] == "reply":
            return ("complaints.reply", complaint_id)
        return ("complaints.index", None)

    def reply(self, complaint_id: int):
        complaint = get_description_by_id(complaint_id)
        if not complaint:
            return ("complaints.index", None)

        reply_text = render_reply_form(complaint)

        if not reply_text:
            return ("complaints.detail", complaint_id)

        add_response(complaint_id, reply_text)
        return ("complaints.detail", complaint_id)

