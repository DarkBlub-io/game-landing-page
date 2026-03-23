from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    game = {
        "name": "Dark Blub",
        "category": "Chiến Lược",
        "developer": "AVA",
        "version": "2.0.1",
        "update_date": "23 Mar 2026",
        "android": "Android 7.0+",
        "description": "Dark Blub là tựa game Chiến Lược mang lại nhiều điều hấp dẫn thú vị.",
        "download_link": "#",
        "play_store_link": "#"
    }

    screenshots = [
    "file_000000004a107209aac97fdf655a9c05.png"
]

    features = [
        "Đồ họa đẹp và mượt",
        "Chiến đấu chiến lược hấp dẫn",
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
