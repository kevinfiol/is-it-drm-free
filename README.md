# is it drm free

```bash
python -m venv venv

source venv/bin/activate
# or on windows
# venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

## Deploy
Create a copy of `.env.defaults` and rename it `.env` with Production environment variables.
```bash
# build image
docker build -t drm .

# run on specified ports `8080:80` where `80` must be defined in .env file
docker run -p 8080:80 drm
```