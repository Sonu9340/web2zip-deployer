
from flask import Flask, render_template, request, send_file
import os
import zipfile
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-apk', methods=['POST'])
def generate_apk():
    app_name = request.form.get('app_name')
    package_name = request.form.get('package_name')
    website_url = request.form.get('website_url')
    # Minimal logic for testing
    zip_id = str(uuid.uuid4())
    output_dir = f"/tmp/{zip_id}"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'README.txt'), 'w') as f:
        f.write(f"App: {app_name}\nPackage: {package_name}\nURL: {website_url}")
    zip_path = f"/tmp/{zip_id}.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(os.path.join(output_dir, 'README.txt'), 'README.txt')
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
