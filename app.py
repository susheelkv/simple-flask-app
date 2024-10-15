from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        vendor_name = request.form.get('name')
        svc_name = request.form.get('svc')
        # For now, just return the inputs
        str1 = "This is the sample text that I want to print.."
        str2 = "This is another sample that I want to print.."
        result = f"Vendor: {vendor_name} Service: {svc_name}"
        # Redirect to result page
        return redirect(url_for('result', result=result))


@app.route('/result')
def result():
    result = request.args.get('result')
    #arg1 = request.args.get('arg1')
    #arg2 = request.args.get('arg2')
    str1 = "This is the sample text that I want to print.."
    str2 = "This is another sample that I want to print.."
    return render_template('result.html', result=result, str1=str1, str2=str2)


if __name__ == '__main__':
    app.run(debug=True)
