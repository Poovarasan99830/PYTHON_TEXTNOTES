



flask_threadpool_images/
│
├── app.py                 <-- Flask entry point (routes/UI)
│
├── workers/               <-- Image processing business logic
│     ├── image_tasks.py   <-- compress + resize functions (Pillow)
│     └── logger.py        <-- simple logging service
│
├── services/              <-- ThreadPoolExecutor layer
│     └── executor_service.py
│
├── static/processed/      <-- Final output images saved here
│
└── templates/             <-- HTML UI
      ├── index.html
      └── results.html





