import requests

# 動画ID（YouTubeの動画IDを指定）
video_id = "dQw4w9WgXcQ"

# invidious APIのエンドポイント
api_url = f"https://inv.nadeko.net/api/v1/videos/{video_id}"

# APIリクエストを送信
response = requests.get(api_url)
video_info = response.json()

# googlevideo.com のリンクをリストから取得
google_video_urls = [stream['url'] for stream in video_info['streams'] if 'googlevideo.com' in stream['url']]

# 最初のURLと最後のURLを取得
if google_video_urls:
    first_url = google_video_urls[0]
    last_url = google_video_urls[-1]

    # 出力
    print(f"${{1-url}}: {first_url}")
    print(f"${{2-url}}: {last_url}")
else:
    print("googlevideo.comのURLは見つかりませんでした。")
