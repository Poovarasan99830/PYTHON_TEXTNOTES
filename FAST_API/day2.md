uvicorn main:app --reload

main → Python file name (main.py)

app → FastAPI instance

--reload → Auto-reload on code changes (useful in development)




uvicorn → Idhu ASGI server. FastAPI application-a run panna use pannuvom. (Django-ku runserver maari, FastAPI-ku uvicorn.)

main → main.py file name. (main.py file irundha main nu mattum kudukkanum.)

app → main.py file-kulla irukkura FastAPI object name. Example: app = FastAPI()

--reload → Code save pannum pothu server automatic-a restart aagum. Development time-la use pannuvom.


uvicorn
   ↓
Open ASGI Server
   ↓
main.py file open pannum
   ↓
app = FastAPI() object find pannum
   ↓
Server start aagum
   ↓
--reload → Code save panna automatic restart aagum




"Uvicorn is an ASGI server used to run FastAPI applications. main is the Python file, app is the FastAPI instance, and --reload automatically restarts the server whenever code changes during development."