from flask  import Flask

app=Flask(__name__)

@app.route("/", methods=["GET"])
def gCont():
    return "This is GET content"

@app.route("/", methods=["POST"])
def pCont():
    return "This is POST contect"

@app.route("/", methods=["PUT"])
def puCont():
    return "This is PUT content"

@app.route("/", methods=["DELETE"])
def delCont():
    return "This is DELETE content"

@app.route("/", methods=["PATCH"])
def patCont():
    return "This is PATCH content"

@app.route("/", methods=["HEAD"])               # This request does not return text on the webpage but [200 OK]
def hCont():
    return "This is HEAD content"

@app.route("/", methods=["OPSTIONS"])           # This request does not return text on the webpage but [200 OK]
def opCont():
    return "This is OPTIONS content"

@app.route("/", methods=["PROPFIND"])
def proCont():
    return "This is PROPFIND content"

@app.route("/", methods=["CUSTOM"])
def cuCont():
    return "This is CUSTOM content"


if __name__=="__main__":
    app.run(debug=True, port=3000)