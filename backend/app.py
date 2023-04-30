from flask import Flask, request, render_template
from model.describe import describeMain
from model.anomaly import main
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/response", methods=["GET", "POST"])
def response():
    if request.method == "POST":
        file = request.files["fileUpload"]
        file.save("./uploads/" + file.filename)
        path = "./uploads/" + file.filename
        information = main(path)
        infoOverpaying = information[1]
        informationText = information[0]

        if infoOverpaying is False:
            overpaying = "Normal"
        else:
            overpaying = "Overpaying"

        response = describeMain(path)
        description = response[0]

        # List of potential procedures
        items = response[1]

        # Use String slicing to split the string into a list of items
        items_list = items.split("\n")

        # Loop over the list and slice each item to remove the number and the dot
        for i in range(len(items_list)):
            items_list[i] = items_list[i][3:]
        del items_list[0:2]

        return render_template(
            "response.html",
            description=description,
            items_list=items_list,
            informationText=informationText,
            infoOverpaying=infoOverpaying,
            overpaying=overpaying,
        )
