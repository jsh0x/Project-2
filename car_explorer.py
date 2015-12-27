from flask import Flask
from flask import render_template
from flask import request
import edmunds

app = Flask(__name__)


api_key = 'rpftuam8pj4dawg5nauq8vs5'
edmunds_api = edmunds.Edmunds(api_key)


@app.route('/', methods=['POST', 'GET'])
def endmonds():
    page_payload = {'models':'', 'makes':'', 'years':''}
    selected = {'make':'', 'model':'', 'year':''}

    if request.method == 'POST':
        form = request.form

        if 'selected_make' in form:
            selected['make'] = request.form['selected_make']
            page_payload['models'] = edmunds_api.get_models(selected['make'])

            if 'selected_model' in form:
                selected['model'] = request.form['selected_model']
                # page_payload['years'] = edmunds_api.get_years(selected['make'], page_payload['model'])
                page_payload['years'] = edmunds_api.get_years(selected['make'], selected['model'])

                if 'selected_year' in form:
                    selected['year'] = request.form['selected_year']


    page_payload['selected'] = selected
    page_payload['makes'] = edmunds_api.get_makes()

    return render_template('car_explorer.html', payload=page_payload)


if __name__ == '__main__':
    app.run(debug=True)