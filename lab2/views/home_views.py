import flask
from lab2.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/")
@response(template_file="home/index.html")
def index() -> dict:
    home_info: str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet blandit tellus. Etiam 
    pulvinar rhoncus nisl, vel elementum magna molestie eu. Aenean blandit lectus sit amet sapien congue iaculis. Nam 
    ac arcu nulla. Duis facilisis mi vitae risus varius eleifend. Praesent elit augue, tristique ac elit sagittis, 
    dictum tempus est. Nunc consectetur eget magna at laoreet. Pellentesque in augue porta, aliquam ex ac, 
    venenatis est. Vivamus blandit odio sed ullamcorper ullamcorper. Sed suscipit egestas nibh eget commodo. Donec 
    placerat finibus pellentesque. Cras consequat metus vitae lorem sodales, ac consequat massa ullamcorper. 
    Suspendisse at tempus diam. """

    return {"home_info": home_info}


@blueprint.route('/about')
@response(template_file='home/about.html')
def about() -> dict:
    return {}


@blueprint.route('/contact_me')
@response(template_file='home/contact_me.html')
def contact_me() -> dict:
    links: list = [
        {"name": "github", "url": "https://github.com/vladhoi"},
        {"name": "linkedin", "url": "https://www.linkedin.com/in/vlad-hoi-6bba8295/"},
    ]

    return {"links": links}
