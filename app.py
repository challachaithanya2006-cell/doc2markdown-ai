from flask import Flask, render_template, request, send_file
from converters.pdf_converter import convert_pdf
from converters.docx_converter import convert_docx
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    file = request.files["file"]

    if not file:
        return "No file selected"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    if file.filename.lower().endswith(".pdf"):
        extracted_text = convert_pdf(filepath)

    elif file.filename.lower().endswith(".docx"):
        extracted_text = convert_docx(filepath)

    else:
        return """
        <h2>❌ Supported Formats: PDF, DOCX</h2>
        <a href="/">Go Back</a>
        """

    markdown_content = f"# {file.filename}\n\n{extracted_text}"

    md_filename = (
        os.path.splitext(file.filename)[0]
        + ".md"
    )

    md_path = os.path.join(
        OUTPUT_FOLDER,
        md_filename
    )

    with open(
        md_path,
        "w",
        encoding="utf-8"
    ) as md_file:
        md_file.write(markdown_content)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Conversion Complete</title>
    </head>
    <body>

    <h1>✅ Conversion Successful</h1>

    <p>
        {file.filename} converted to Markdown.
    </p>

    <a href="/download/{md_filename}">
        Download Markdown File
    </a>

    <br><br>

    <a href="/">
        Convert Another File
    </a>

    </body>
    </html>
    """


@app.route("/download/<filename>")
def download_file(filename):

    file_path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    return send_file(
        file_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)