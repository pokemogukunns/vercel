from flask import Flask, render_template
import requests
import logging


app = Flask(__name__)




logging.basicConfig(level=logging.DEBUG)


@app.route('/videos/<video_id>')
def video(video_id):
    # Invidious APIから動画情報を取得
    api_url = f"https://youtube.privacyplz.org/api/v1/videos/{video_id}"
    response = requests.get(api_url)
    video_info = response.json()

    # googlevideo.comのリンクをリストから取得
    google_video_urls = [stream['url'] for stream in video_info['streams'] if 'googlevideo.com' in stream['url']]
    
    # 最初と最後のURLを取得
    if google_video_urls:
        first_url = google_video_urls[0]
        last_url = google_video_urls[-1]
    else:
        first_url = last_url = ""

    # テンプレートに渡す
    return render_template('video.html', first_url=first_url, last_url=last_url)

if __name__ == '__main__':
    app.run(debug=True)

