from project import app

@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def chrome_devtools():
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)

