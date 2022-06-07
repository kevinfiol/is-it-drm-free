# is it drm free

Find DRM-Free games easier. The main instance runs off a Raspberry Pi 4 in my office, so excuse any downtime.

**If you like this, check out my userscript for Steam, [its-drm-free](https://github.com/kevinfiol/its-drm-free).**

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

## To-do
* ITAD has a lot of redundant search results. Instead of auto-directing to the top result, I think it'd be better to show a list of results (maybe top 5 or whatever). Kind of defeats the original idea, but would be more usable.
