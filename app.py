from flask import Flask, request, jsonify
import deezer

app = Flask(__name__)
client = deezer.Client()

@app.route('/')
def index():
    return jsonify({"status": "online", "message": "High-Res Music Engine is running"})

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
  
