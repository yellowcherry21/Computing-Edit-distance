from flask import Flask, request, render_template


def edit_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        q = 0
        if s[len(s)-1] != t[len(t)-1]:
            q = 1
        d1 = int(edit_distance(s.rstrip(s[len(s)-1]), t)) + 1
        d2 = int(edit_distance(s, t.rstrip(t[len(t)-1]))) + 1
        d3 = int(edit_distance(s.rstrip(s[len(s)-1]), t.rstrip(t[len(t)-1]))) + q
        return min(d1, d2, d3)


app = Flask(__name__)
results = []


@app.route('/', methods=['GET', 'POST'])
def solution():
    if request.method == 'POST':
        String1 = request.form['String1']
        String2 = request.form['String2']
        return '<h1>The edit distance between "{}", and "{}" is {}</h1>'.format(String1, String2, edit_distance(String1, String2))
    return render_template('edist.html')
