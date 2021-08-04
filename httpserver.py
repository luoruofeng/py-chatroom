from flask import Flask,render_template,request

#Flask will look for templates in the templates folder.
flask_app = Flask(import_name=__name__,
            static_url_path='/static', # 配置静态文件的访问 url 前缀
            static_folder='ui',    # 配置静态文件的文件夹
            template_folder='ui/html') # 配置模板文件的文件夹

@flask_app.route("/")
def home():
    return render_template("home.html")

@flask_app.route("/index")
def index():
    return render_template("index.html")

@flask_app.route("/test")
def test():
    return render_template("test.html")

if __name__ == '__main__':
    flask_app.run("0.0.0.0", 8888)