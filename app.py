from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello App</title>
    </head>
    <body>
        <h1>ようこそ！</h1>
        <input type="text" id="nameInput" placeholder="名前を入力してください">
        <button onclick="sayHello()">送信</button>

        <script>
            function sayHello() {
                const name = document.getElementById("nameInput").value;
                if (name.trim() === "") {
                    alert("名前を入力してください！");
                } else {
                    alert("こんにちは、" + name + "さん！");
                }
            }
        </script>
    </body>
    </html>
    """)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)