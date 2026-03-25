from flask import Flask, render_template, request
import instaloader
import re

app = Flask(__name__)

# Instagram loader setup
L = instaloader.Instaloader()

def get_reel_url(url):
    try:
        # Link se shortcode nikalne ke liye (e.g., C4d5gh7jK)
        shortcode_match = re.search(r'/(?:reel|p|reels)/([A-Za-z0-9_-]+)/', url)
        if not shortcode_match:
            return None, "Invalid Link! Sahi link paste karein."
        
        shortcode = shortcode_match.group(1)
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        if post.is_video:
            return post.video_url, None
        else:
            return None, "Ye video nahi hai!"
    except Exception as e:
        return None, f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def home():
    video_link = None
    error = None
    if request.method == 'POST':
        user_url = request.form.get('url')
        video_link, error = get_reel_url(user_url)
        
    return render_template('index.html', video_link=video_link, error=error)

if __name__ == '__main__':
    app.run(debug=True)