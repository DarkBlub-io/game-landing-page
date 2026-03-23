from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    game = {
        "name": "Shadow Arena",
        "category": "Hành động",
        "developer": "Storm Studio",
        "version": "2.0.1",
        "update_date": "23 Mar 2026",
        "android": "Android 7.0+",
        "description": "Shadow Arena là tựa game hành động hấp dẫn với đồ họa đẹp, chiến đấu tốc độ cao và nhiều chế độ chơi thú vị.",
        "download_link": "#",
        "play_store_link": "#"
    }

    screenshots = [
        "images/shot1.jpg",
        "images/shot2.jpg",
        "images/shot3.jpg"
    ]

    features = [
        "Đồ họa đẹp và mượt",
        "Nhiều chế độ chiến đấu",
        "Tùy chỉnh nhân vật",
        "Tối ưu cho nhiều máy Android"
    ]

    return render_template(
        "index.html",
        game=game,
        screenshots=screenshots,
        features=features
    )

if __name__ == "__main__":
    app.run(debug=True)
