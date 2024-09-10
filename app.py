from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from ikigai_chart import generate_ikigai_diagram

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'what_you_love': request.form['what_you_love'].split(','),
            'what_the_world_needs': request.form['what_the_world_needs'].split(','),
            'what_you_can_be_paid_for': request.form['what_you_can_be_paid_for'].split(','),
            'what_you_are_good_at': request.form['what_you_are_good_at'].split(',')
        }
        return render_template('review.html', data=data)
    return render_template('index.html')

@app.route('/review', methods=['POST'])
def review():
    if request.form['action'] == 'generate':
        data = {
            'what_you_love': request.form['what_you_love'].split(','),
            'what_the_world_needs': request.form['what_the_world_needs'].split(','),
            'what_you_can_be_paid_for': request.form['what_you_can_be_paid_for'].split(','),
            'what_you_are_good_at': request.form['what_you_are_good_at'].split(',')
        }
        image_path = generate_ikigai_diagram(data, app.config['UPLOAD_FOLDER'])
        return render_template('result.html', image_path=image_path)
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
