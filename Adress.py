import flask

app = flask.Flask("Adress")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content


def get_Adress():
    listdb = open("list.txt")
    content = listdb.read()
    listdb.close()
    Adress = content.split("\n") 
    Adress.sort()
    return Adress

@app.route("/Guests")
def Guests():
    html_page = get_html("Guests")
    Adress = get_Adress()
    actual_values = ""
    for Names in Adress:
        actual_values += "<p>" + Names + "</p>"
    return html_page.replace("$$Adress_Book$$", actual_values)


@app.route("/")
def Homepage():
    return get_html("index")

