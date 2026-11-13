## **File Uploads / Downloads – Interview Notes (Quick Revision)**

* **File Uploads/Downloads** in **FastAPI** allow users to **upload** files using **`UploadFile`** and **`File`**, and **download** files using **`FileResponse`**.
* Purpose: Handle **documents**, **images**, **PDFs**, **Excel files**, and other files efficiently for processing or downloading.
* **Working Flow:** **Client Uploads File → FastAPI Receives File → Process/Store File → Return Response or Download File**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, customers uploaded **insurance documents** (Policy PDF, Aadhaar, Driving License, Medical Reports, Claim Images). FastAPI stored the files, triggered **OCR** for text extraction, and later allowed users to **download** claim reports and settlement documents.
* **Code:**

```python
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.get("/download")
def download_file():
    return FileResponse("claim_report.pdf")
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, users uploaded claim-related documents through FastAPI using **`UploadFile`**. The uploaded files were processed by the **OCR service** to extract policy details and claim information. After claim processing was completed, FastAPI provided **downloadable claim reports**, **approval letters**, and **settlement documents** using **`FileResponse`**.
