import flask

# do __name__.split('.')[0] if initialising from a file not at project root
app = flask.Flask(__name__)

# Error handling and helpers
#
def error_info(e):
    content = ""
    try:  # it's probably a HttpException, if you're using the bigcommerce client
        content += str(e.headers) + "<br>" + str(e.content) + "<br>"
        req = e.response.request
        content += (
            "<br>Request:<br>"
            + req.url
            + "<br>"
            + str(req.headers)
            + "<br>"
            + str(req.body)
        )
    except AttributeError as e:  # not a HttpException
        content += "<br><br> (This page threw an exception: {})".format(str(e))
    return content


@app.errorhandler(500)
def internal_server_error(e):
    content = "Internal Server Error: " + str(e) + "<br>"
    content += error_info(e)
    return content, 500


@app.errorhandler(400)
def bad_request(e):
    content = "Bad Request: " + str(e) + "<br>"
    content += error_info(e)
    return content, 400


# Helper for template rendering
def render(template, context):
    return flask.render_template(template, **context)


#
# App interface
#
@app.route("/")
def index():
    # Render page
    context = dict()
    context["user"] = {
        "name": "John Doe",
        "email": "Justin",
    }
    context["menu"] = MENU
    return render("index.html", context)


@app.route("/make-drink")
def makeDrink(drink):
    # Render page
    context = dict()
    context["user"] = {
        "name": "John Doe",
        "email": "Justin",
    }
    context["menu"] = MENU
    return render("index.html", context)

MENU = {
    "drinks": [
        {
            "name": "Coffee",
            "description": "Hot coffee",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://picsum.photos/150/150",
        },
        {
            "name": "Tea",
            "description": "Hot tea",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://picsum.photos/150/150",
        },
        {
            "name": "Cappuccino",
            "description": "Hot cappuccino",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://picsum.photos/150/150",
        },
        {
            "name": "Latte",
            "description": "Hot latte",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://picsum.photos/150/150",
        },
        {
            "name": "Mocha",
            "description": "Hot mocha",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://picsum.photos/150/150",
        },
    ]
}

if __name__ == "__main__":
    app.run("localhost", "8080")
