from flask import Flask, request, render_template_string, send_from_directory
import os

app = Flask(__name__)

# List to store reported data
reports = []

# HTML template for displaying the data
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orb Sentinel</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
</head>
<body>
    <h1>Orb Sentinel</h1>
    <table border="1" style="width: 100%; text-align: left;">
        <thead>
            <tr>
                <th>Image</th>
                <th>Time</th>
                <th>Device</th>
            </tr>
        </thead>
        <tbody>
            {% for report in reports %}
            <tr>
                <td>{{ report.image }}</td>
                <td>{{ report.time }}</td>
                <td>{{ report.device }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    if data:
        reports.append(data)
        print(f"Received data: {data}")
    return {"status": "success"}, 200


@app.route("/")
def home():
    return render_template_string(html_template, reports=reports)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
