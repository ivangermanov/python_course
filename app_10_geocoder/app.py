from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
from geopy.geocoders import GoogleV3
import pandas
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success/", methods=["POST"])
def success():
    global filename
    if request.method == "POST":
        file = request.files["file_name"]
        try:
            if file.filename.lower().endswith('.csv') == True:
                df = pandas.read_csv(file.filename)
                print(df)
                if 'Address' in df.columns:
                    nom = GoogleV3(
                        api_key="AIzaSyAv2OOloU7-ZoO_iQ86u_Y934K96o_3_sw")
                    df["Coordinates"] = df["Address"].apply(nom.geocode)
                    df["Latitude"] = df["Coordinates"].apply(
                        lambda x: x.latitude if x != None else None)
                    df["Longitude"] = df["Coordinates"].apply(
                        lambda x: x.longitude if x != None else None)
                    df = df.drop("Coordinates", 1)
                    filename = datetime.datetime.now().strftime(
                        "%Y-%m-%d-%H-%M-%S-%f"+".csv")
                    df.to_csv(filename, index=None)
                    return render_template("success.html", data=df.to_html(justify="match-parent"), btn="download.html")
                elif "address" in df.columns:
                    nom = GoogleV3(
                        api_key="AIzaSyAv2OOloU7-ZoO_iQ86u_Y934K96o_3_sw")
                    df["Coordinates"] = df["address"].apply(nom.geocode)
                    df["Latitude"] = df["Coordinates"].apply(
                        lambda x: x.latitude if x != None else None)
                    df["Longitude"] = df["Coordinates"].apply(
                        lambda x: x.longitude if x != None else None)
                    df = df.drop("Coordinates", 1)
                    filename = datetime.datetime.now().strftime(
                        "%Y-%m-%d-%H-%M-%S-%f"+".csv")
                    df.to_csv(filename, index=None)
                    return render_template("success.html", data=df.to_html(justify="match-parent", btn="download.html"))
                else:
                    return render_template("index.html", msg="Please make sure you have an address column in your csv file!")
            else:
                return render_template("index.html", msg="Please import a .csv file!")
        except:
            return render_template("index.html", msg="Please import a .csv file!")


@app.route("/download/")
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()
