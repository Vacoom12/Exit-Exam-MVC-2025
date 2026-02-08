from src.models.stalls_model import *
from src.views.stalls_view import *

class StallsController:
    def index(self):
        rows = get_complaint_count_each_stall()
        action = render_stalls_page(rows)

        return ("home", None)