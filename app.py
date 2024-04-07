import psutil
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    percent_cpu = psutil.cpu_percent()
    percent_mem = psutil.virtual_memory().percent
    message = None
    if percent_cpu > 80 or percent_mem > 80:
        message = "High utlization of Memory or CPU."
    #return f"CPU Utilization: {percent_cpu} and Memory utilization: {percent_mem}"
    return render_template("index.html",cpu_metric=percent_cpu,mem_metric=percent_mem,message=message)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')