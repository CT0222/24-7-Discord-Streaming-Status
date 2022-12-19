from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def main():
    return '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script src="https://cdn.tailwindcss.com"></script>
  <body class="bg-gray-900">
      <div class="flex py-5 justify-center">
        <div class="btns py-8">
          <a href="https://youtube.com/ct02yt" class="btn"><button class="bg-red-600 text-white rounded h-12 pr-8 pl-8 w-fit transition hover:translate-y-1 hover:brightness-125"><i class="fab fa-youtube"></i></button></a>
        </div>
      </div>
    </div>
  </body>'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
