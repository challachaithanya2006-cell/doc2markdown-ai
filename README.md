# 🚀 Doc2Markdown AI

> AI-powered document conversion platform that transforms PDFs, Word documents, PowerPoint presentations, Excel spreadsheets, and images into clean, structured Markdown with OCR and AI-powered summarization.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![OpenAI](https://img.shields.io/badge/OpenAI-AI%20Powered-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

Doc2Markdown AI is a document processing application designed to convert multiple file formats into Markdown, making content easier to analyze, summarize, and integrate into AI workflows.

The project combines document parsing, OCR, and AI-based summarization to create a streamlined document-to-Markdown pipeline.

---

## ✨ Features

* 📄 PDF to Markdown Conversion
* 📝 DOCX to Markdown Conversion
* 📊 Excel to Markdown Conversion
* 📽️ PowerPoint to Markdown Conversion
* 🖼️ Image OCR to Markdown
* 🤖 AI-Powered Text Summarization
* ⚡ Fast and Lightweight Processing
* 🔌 Modular Converter Architecture
* 📥 Download Generated Markdown

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Document Processing

* PyPDF2
* python-docx
* python-pptx
* openpyxl

### OCR

* Tesseract OCR
* Pillow

### AI Integration

* OpenAI API

---

## 📂 Project Structure

```text
doc2markdown-ai/
│
├── app.py
│
├── converters/
│   ├── pdf_converter.py
│   ├── docx_converter.py
│   ├── pptx_converter.py
│   ├── xlsx_converter.py
│   └── image_converter.py
│
├── ai/
│   └── ai_summarizer.py
│
├── templates/
├── static/
├── uploads/
├── output/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/challachaithanya2006-cell/doc2markdown-ai.git
cd doc2markdown-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🎯 Use Cases

* AI Knowledge Bases
* Research Document Processing
* Resume Parsing
* Academic Content Extraction
* OCR Text Extraction
* Markdown Content Generation
* LLM Data Preparation

---

## 🔮 Future Enhancements

* Drag & Drop File Upload
* Batch File Processing
* User Authentication
* Cloud Storage Integration
* Multi-Language OCR
* REST API Support
* Docker Deployment
* Dark Mode Interface

---

## 👨‍💻 Author

**Challa Naga Chaitanya Sai**

* GitHub: https://github.com/challachaithanya2006-cell
* LinkedIn: Add your LinkedIn profile here

---

## 📄 License

This project is licensed under the MIT License.
