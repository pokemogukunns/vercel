import yt_dlp
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/getStreamUrl', methods=['POST'])
def get_stream_url():
    video_url = request.json.get('url')

    if not video_url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,  # ダウンロードせずにURLのみ取得
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(video_url, download=False)
            # 動画のストリームURLを取得
            stream_url = result.get('url', None)

            if stream_url:
                return jsonify({'streamUrl': stream_url})
            else:
                return jsonify({'error': 'Failed to retrieve stream URL'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
