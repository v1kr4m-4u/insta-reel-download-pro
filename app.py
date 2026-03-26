from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        # User jo link paste karega wo yahan aayega
        reel_link = request.form.get('url')
        
        # --- Yahan apna Instagram scraping logic likhein ---
        # Abhi ke liye main ek sample video link de raha hoon test karne ke liye
        # Jab aapka logic ready ho, toh 'video_url' mein actual MP4 link daal dena
        video_url = "https://www.w3schools.com/html/mov_bbb.mp4" 

    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
