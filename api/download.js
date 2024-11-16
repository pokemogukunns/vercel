const ytDlp = require('yt-dlp');

module.exports = async (req, res) => {
  const { url } = req.query;

  if (!url) {
    return res.status(400).json({ error: 'URL is required' });
  }

  try {
    // yt-dlpで動画のメタデータを取得
    const videoInfo = await ytDlp.getInfo(url);
    
    // 最適なダウンロードリンクを取得（例: googlevideo.com）
    const format = videoInfo.formats.find(f => f.url && f.url.includes('googlevideo.com'));

    if (!format) {
      return res.status(404).json({ error: 'No valid download link found' });
    }

    // ダウンロードリンクを返す
    res.json({ download_link: format.url });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error processing the video' });
  }
};
