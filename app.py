from dotenv import load_dotenv
from flask import  Flask, render_template, request, jsonify

from ice_breaker import get_brief_information

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/submit", methods=["POST"])
def process():
    name = request.form.get("username")
    if not name:
        # no input — show the home with a small error
        return render_template("index.html", error="Please enter a name.")
    try:
        summary_obj, profile_pic_url, first_name, last_name = get_brief_information(name=name)
    except Exception as e:
        app.logger.exception("get_brief_information failed")
        summary_obj, profile_pic_url, first_name, last_name = None, None, "", ""

    summary_text = getattr(summary_obj, "summary", None) if summary_obj else None
    facts = getattr(summary_obj, "facts", []) if summary_obj else []

    not_found = not any([summary_text, facts, profile_pic_url, first_name, last_name])
    return render_template(
        "result.html",
        name=first_name or ""+ " " + last_name or "",
        summary=summary_text,
        facts=facts,
        photo=profile_pic_url,
        not_found=not_found
    )

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
