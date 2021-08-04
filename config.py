HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = "7693805"
    API_HASH = "9119a2d0d247cec7a3063b13b663effe"
    ARQ_API_KEY = "WWQTKT-XFMJOT-HPMRFX-GOUUWS-ARQ"
    CHAT_ID = "-1001180648994"
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"saavn"

# don't make changes below this line
ARQ_API = "https://thearq.tech"
