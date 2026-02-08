from src.controllers.complaints_controller import ComplaintsController
from src.controllers.stalls_controller import StallsController

class Router:
    def __init__(self):
        self.complaints = ComplaintsController()
        self.stalls = StallsController()

        self.routes = {
            "complaints.index": lambda arg: self.complaints.index(),
            "complaints.detail": lambda arg: self.complaints.detail(arg),
            "complaints.reply": lambda arg: self.complaints.reply(arg),
            "stalls.index": lambda arg: self.stalls.index(),
        }

    def dispatch(self, route_name: str, arg):
        handler = self.routes.get(route_name)
        if not handler:
            return ("home", None)
        return handler(arg)
