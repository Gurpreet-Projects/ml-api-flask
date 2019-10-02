import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
model = pickle.load(open('model.pkl', 'rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])
def predict():
    # print('predict()')

    # get data
    data = request.get_json(force=True)

    # convert data into data frame
    data.update((x, [y]) for x, y in data.items())

    # create a data frame
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # sent back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)