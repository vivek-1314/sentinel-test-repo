def render_home(user):
    return f"<h1>Welcome {user}</h1>"


def render_cart(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
