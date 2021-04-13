# is it drm free

Find DRM-Free games easier.

## Run
Create a copy of `.env.dev` and rename it to `.env` with Development environment variables.
```bash
python -m venv venv

# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate.bat

pip install -r requirements.txt
python app.py
```

## Build & Run with Docker
Create a copy of `.env.prod` and rename it to `.env` with Production environment variables.
```bash
# build image
docker build -t drm .

# run on specified ports `8080:80` where `80` must be defined in .env file
docker run -p 8080:80 drm
```