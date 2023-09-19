from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import tesseract
import os

UPLOAD_FOLDER = r'C:\Users\Kamden\Developer\OCR\flask-server\files\Uploads'
DOWNLOAD_FOLDER = r'C:\Users\Kamden\Developer\OCR\flask-server\files\Downloads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg' }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/convert", methods=["POST", "GET"])
@cross_origin()
def convert():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):

            # save file to upload folder
            filename = secure_filename(file.filename)
            uploadPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(uploadPath) 

            # create name and path for the file that client will download
            downloadName = "searchable-" + filename
            downloadPath = os.path.join(DOWNLOAD_FOLDER, downloadName)
            print(downloadName)
            tesseract.convertPdf(uploadPath, downloadPath)
            return send_file(downloadPath, download_name=downloadName)
        

if __name__ == "__main__":
    app.run(debug=True)

