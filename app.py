from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {"name": "Python", "category": "Programming"},
    {"name": "Java", "category": "Programming"},
    {"name": "AWS", "category": "Cloud Computing"},
    {"name": "Linux", "category": "Operating Systems"},
    {"name": "Docker", "category": "DevOps"},
    {"name": "Jenkins", "category": "DevOps"},
    {"name": "Kubernetes", "category": "DevOps"},
    {"name": "Git and GitHub", "category": "DevOps"},
    {"name": "HTML and CSS", "category": "Web Development"},
    {"name": "JavaScript", "category": "Web Development"},
    {"name": "SQL and MySQL", "category": "Database"},
    {"name": "Machine Learning", "category": "AI & ML"},
]

@app.route("/")
def home():
    return render_template("index.html", courses=courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
