from flask import Flask, render_template, request, redirect

from helpers import parse_aln, parse_clw, parse_fst

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/view", methods=["GET", "POST"])
def sequence():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.clw'):
            sequences = parse_clw(file)
            return render_template('sequence.html', sequences=sequences)
        elif file.filename.endswith('.aln'):
            sequences = parse_aln(file)
            return render_template('sequence.html', sequences=sequences)
        elif file.filename.endswith('.fst') or file.filename.endswith('.fsta'):
            sequences = parse_fst(file)
            return render_template('sequence.html', sequences=sequences)

    return redirect("/")

