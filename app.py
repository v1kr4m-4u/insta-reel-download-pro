from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)
L = instaloader.Instaloader()

def get_insta_video_url(share_url):
    try:
        # Link se shortcode nikalna (e.g., C6jK8...)
        shortcode = share_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        return post.video_url
    except Exception as e:
        print(f"Error fetching video: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        reel_link = request.form.get('url')
        if reel_link:
            # Ab yahan asli link fetch hoga!
            video_url = get_insta_video_url(reel_link)
            
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
