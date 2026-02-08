from src.routes.router import Router
from src.views.home_view import render_home_menu

def main():
    router = Router()

    route_name = "home"
    arg = None

    while True:
        if route_name == "home":
            c = render_home_menu()
            if c == "0":
                print("ออกจากโปรแกรม")
                break
            if c == "1":
                route_name, arg = ("complaints.index", None)
            elif c == "2":
                route_name, arg = ("stalls.index", None)
            continue

        route_name, arg = router.dispatch(route_name, arg)


if __name__ == "__main__":
    main()
