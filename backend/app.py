from flask import Flask, render_template
from api.routes import game_routes

# ✅ Ensure Flask knows where the templates and static files are
app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")

# ✅ Fix: Serve the actual HTML file instead of plain text
@app.route('/')
def home():
    return render_template('index.html')  # ✅ Ensure index.html is rendered

# Register game API routes
app.register_blueprint(game_routes, url_prefix='/game')

if __name__ == '__main__':
    app.run(debug=True)
