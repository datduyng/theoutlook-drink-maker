import flask
from flask import jsonify
from flask import request

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


@app.route("/make-drink", methods=["POST"])
def makeDrink():
    data = request.data  # data is empty
    # Render page
    print('Making drink', data)

    ########## JUSTIN BECKER'S CODE ##########
    # return json 
    return jsonify(success = True);

MENU = {
    "config": {
        "confirmation1": "Place cup in the cup holder:",
        "confirmation2": "Confirm where the emergency stop",
    },
    "drinks": [
        {
            "name": "Lemon Drop",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh6.googleusercontent.com/JeGSDNCbKgVGjDs4JfLkR64S3Eg_nLYUu0wS1283uLHdUgw_wPx6ciKmwmqZLV52h4avRrlLOMNivnG-kAqV1hqWf6deWY2rPY2uxwk4S2ioYJy51FIb9KCEcyosUjy9H6-1om8bsRJk1tiQNeZV3PxB_vOgmMofYgz6Zhc1kNkLGQrHpk2I_f-nEQ?alr=yes",
        },
        {
            "name": "Dark& Stormy",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh5.googleusercontent.com/Q4IOOcEauPMNhpG3mEmUp04hNQ2CF90RPrWCWkI0BEOo99ypC-KYdZNKkwQmJq8SDbTpwOqFi-WPR4rN9xj5aOycLSH1bt7ADUBFtZ0u2uqtb8_Zeqb-QH-ZaGkLBiDeYnjC0NZb1iqe7OVXBvhFNJlLjfANujUUQnvLhN1dAMdssoswaO5nD4hdPw?alr=yes",
        },
        {
            "name": "Tom Collins",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh3.googleusercontent.com/aE4t5-F2getbVzoMTV6MCLThNdapznPSM5uJdhDCiW5q1jPxTQpjhy8FXj12jsrSkFW0KKrldibPIzZYZEFnHGBkxLFzGXYjK7cb9WOiNsfcStPVZnKFzngobTzgUJGFXy6o0eJTaNd1M3Rz3CHnxQpx5vkepaH6whiwAikfx4WL_3myScTtylTS2g?alr=yes",
        },
        {
            "name": "Moscow Mule",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh5.googleusercontent.com/K8ObMl8s9t7VWIL6WEW5XwxiluUloMLQPTI2Tir1am1OeRAY88ZWnQA7BG4EKotfz2uvqz1W_hFUvr9fi1gULOW8B6aV6EegKDBPnhoVEjbcuaT2U5sTm13W53Jb4QLMVnxeO28ERXwqGhmKpyAgcK_t-8RaKE8mVIlS7q9EL30b3gIL6xqw6XA8bQ?alr=yes",
        },
        {
            "name": "Cosmo",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh6.googleusercontent.com/E30JIjz2Dn0SH85MjZjkpRuTtY54e_W-dxctPWsV1YisRT-roJmsHVXWwQgpRA1CIQzZLRxVpNUCoEs5WPK9qSsTtEXfbHg3b2Hq3U3_7iPWVrf64o4FWxp7O0_ryl8H_QRPy_h_l1SMC7fx0VMAqYzEe043j7p4TNXDbS6J-oyR0DQg01ideD4UDQ?alr=yes",
        },

        {
            "name": "Tequila Sunrise",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh5.googleusercontent.com/tQe-0XkbfROspJ62ulFXGubkdV5GnLBz950o3W5kpEPxu_CT9C3vtqvYPp5IlmSb0kM6v8oTqKyRnWcp02_V2mmXpsJT990aJJAuQTpkZ1rtl355wHS7N5ywvpwWWcsGbRYTTtR_6nWsxn0P54_9h2nQhIeWTDht-kJmxwWDSozJmbyGRXYMD1JnOA?alr=yes",
        },

        {
            "name": "Daiquiri",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh3.googleusercontent.com/Bc29cckYAwYqb-fLf1L-SmF2icUh0JSh2jNVv2wVGZ1Ay0JYXVbKtcp6r8OqRyRvcMIpmz-vbycaWqmLkhrBPwr_YMyjPuuW_3x7J1-V0DI0GkL2pC2pzTsptIAXkUrpnhJnXh1Lkd-KpVgEtPxSQxDJddvTdxpJGycX2xJaXXOZh63f4kPIRzs1vQ?alr=yes",
        },
        {
            "name": "Margarita",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh5.googleusercontent.com/FzfC38zvgELzSg6vYERtrchIwR4ZTYucxClEXx-HnwInCBhcn3m51kflfe8Yg-8cbaGxEtzU7fz7NvTcBx7Wmk8gpXiyKFeRw2GLjr1CLrJkppaN3pwQbgM50-xReTRffpBOAmVLtwq-R7jGx3MjVF3nxnHEvCYggfhWgE3usgB8FCcdQJuBbY8muA?alr=yes",
        },
        {
            "name": "Long Island Iced Tea",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh4.googleusercontent.com/2iESC3ApLuBDWVtbwJbwlME5zoZQs-QB4YpaMvAUuj_1hE6O0anEGSwvy45nrZFZLZHFbltNGaKYrLTYHQoorKXN5O-shDyW0ne08SHGio4JM9ZVScKXILeTPOuldqqXJihRUi5rq3EqepvLgf2lmltDwA1Z11LsbDbLSackP_hriJed3-y7mmmD_w?alr=yes",
        },
        {
            "name": "Rum & Coke",
            "description": "",
            "ingredients": ["2 shot of expresso", "hot water", "milk"],
            "image": "https://lh6.googleusercontent.com/NwQnU-yqf0nwCRFNePYbPwImJ1e-lj--DIlwB_Z3zW41E8nc9PzDIKbHyhmtcC6EYKqu8-o3wePQ4wlWMo4d3DNFLWAZAcAOKVoMWV8crTydcXMhuLef3fWO7DbQhCyyiHYqmARPG_VTy-h1JwjpMxJIzh6xKY0AyzH1djJnQxXt_wePZaQbyn8hWA?alr=yes",
        },
    ]
}

if __name__ == "__main__":
    app.run("localhost", "8080")
