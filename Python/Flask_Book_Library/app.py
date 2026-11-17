from project import app


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def chrome_devtools():
    return '', 204