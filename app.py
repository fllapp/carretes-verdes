from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ppt')
def show_ppt():
    # URL del archivo de presentación de PowerPoint en OneDrive
    ppt_url = "https://1drv.ms/p/s!AtWfS3AxQSUmiVA579jEfmJUmqTt?e=DEAp8e"

    # Renderizar la plantilla 'index.html' y pasar la URL del archivo
    return render_template('index.html', ppt_url=ppt_url)

@app.route('/terms_conditions')
def terms_conditions():
    return render_template('terms_conditions.html')

if __name__ == '__main__':
    app.run(debug=True)
