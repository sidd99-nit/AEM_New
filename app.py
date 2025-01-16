from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample data to simulate a database or data source
tiles_data = [
    {"id": 1024, "name": "Coca-Cola - Original Taste", "images": ["/static/images/img1.jpg", "/static/images/img2.jpg", "/static/images/img3.jpg"]},
    {"id": 5050, "name": "Yakult - Probiotic Drink", "images": ["/static/images/img4.jpg", "/static/images/img5.jpg", "/static/images/img6.jpg"]},
    {"id": 8080, "name": "Kurkure - Naughty Tomato", "images": ["/static/images/img7.jpg", "/static/images/img8.jpg", "/static/images/img9.jpg"]},
    {"id": 5000, "name": "Oreo - Mega Family Pack", "images": ["/static/images/img10.jpg", "/static/images/img11.jpg", "/static/images/img12.jpg"]},
    {"id": 3000, "name": "Lays - Chili Lime Flavor", "images": ["/static/images/img13.jpg", "/static/images/img14.jpg", "/static/images/img15.jpg"]},
    {"id": 9090, "name": "Red Bull - Energy Drink", "images": ["/static/images/img16.jpg", "/static/images/img17.jpg", "/static/images/img18.jpg"]},
    {"id": 7021, "name": "Kellogg's Cornflakes - Original", "images": ["/static/images/img19.jpg", "/static/images/img20.jpg", "/static/images/img21.jpg"]},
    {"id": 1025, "name": "Coca-Cola - Vanilla", "images": ["/static/images/img22.jpg", "/static/images/img23.jpg", "/static/images/img24.jpg"]},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tiles', methods=['GET'])
def get_tiles():
    return jsonify(tiles_data)

@app.route('/gallery/<int:tile_id>')
def gallery(tile_id):
    tile = next((tile for tile in tiles_data if tile["id"] == tile_id), None)
    if not tile:
        return "Tile not found", 404
    return render_template('gallery.html', tile=tile)

if __name__ == '__main__':
    app.run(debug=True)
