
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_connection

app = Flask(__name__)

# Allow frontend to communicate with backend
CORS(app)


# Convert database row into API response
def format_site(site):
    return {
        "id": site["id"],
        "name": site["name"],
        "target": site["target"],
        "extraterrestrial_match": site["extraterrestrial_match"],
        "coords": [
            site["latitude"],
            site["longitude"]
        ],
        "terrain": site["terrain"],
        "similarity_score": site["similarity_score"],
        "traits": site["traits"],
        "testing": site["testing"],
        "nasa_dataset": site["nasa_dataset"],
        "nasa_url": site["nasa_url"]
    }


# Home API
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "TerraSpace Analog Explorer",
        "status": "Backend is running",
        "database": "SQLite",
        "total_sites": 6
    })


# Get all locations
@app.route("/api/sites", methods=["GET"])
def get_all_sites():
    conn = get_connection()

    sites = conn.execute(
        "SELECT * FROM sites"
    ).fetchall()

    conn.close()

    return jsonify([format_site(site) for site in sites])


# Get a particular location using ID
@app.route("/api/sites/<site_id>", methods=["GET"])
def get_site(site_id):
    conn = get_connection()

    site = conn.execute(
        "SELECT * FROM sites WHERE id = ?",
        (site_id.upper(),)
    ).fetchone()

    conn.close()

    if site is None:
        return jsonify({"error": "Location not found"}), 404

    return jsonify(format_site(site))


# Get Moon locations
@app.route("/api/moon", methods=["GET"])
def get_moon_sites():
    conn = get_connection()

    sites = conn.execute(
        "SELECT * FROM sites WHERE target = ?",
        ("Moon",)
    ).fetchall()

    conn.close()

    return jsonify([format_site(site) for site in sites])


# Get Mars locations
@app.route("/api/mars", methods=["GET"])
def get_mars_sites():
    conn = get_connection()

    sites = conn.execute(
        "SELECT * FROM sites WHERE target = ?",
        ("Mars",)
    ).fetchall()

    conn.close()

    return jsonify([format_site(site) for site in sites])


# Search locations by name or ID
@app.route("/api/search", methods=["GET"])
def search_sites():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify({"error": "Please enter a search term"}), 400

    conn = get_connection()

    sites = conn.execute("""
        SELECT * FROM sites
        WHERE name LIKE ? OR id LIKE ?
    """, (
        "%" + query + "%",
        "%" + query + "%"
    )).fetchall()

    conn.close()

    return jsonify([format_site(site) for site in sites])


# Run backend
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
