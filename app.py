from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    grade_value = ""

    if request.method == "POST":
        grade_value = request.form.get("txtGrade", "").strip()

        try:
            grade = float(grade_value)
            if grade < 0 or grade > 100:
                answer = "La nota debe estar entre 0 y 100."
            elif grade >= 60:
                answer = f"Aprobado con {grade}"
            else:
                answer = f"Reprobado con {grade}"
        except ValueError:
            answer = "Por favor ingresa un número válido."

    return render_template("index.html", answer=answer, grade_value=grade_value)

if __name__ == "__main__":
    app.run(debug=True)