from flask import Flask, request, jsonify, send_from_directory
import deezer
import os

app = Flask(__name__, static_folder='.') # '.' ka matlab isi folder mein HTML hai

client = deezer.Client()

# Home route jo HTML file dikhayega
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/search')
def search_music():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    try:
        results = client.search(query)
        music_list = []
        for track in results:
            music_list.append({
                "track_id": track.id,
                "title": track.title,
                "artist": track.artist.name,
                "cover": track.album.cover_big,
                "preview_url": track.preview
            })
        return jsonify(music_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
    
