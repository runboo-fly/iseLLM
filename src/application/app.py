from flask import Flask, request, jsonify

from src.service.unitTestGenerate import unit_test_generate

app = Flask(__name__)


@app.route('/codeGenerate/ut', methods=['POST'])
def generate_unit_test():
    try:
        data = request.json
        if 'code' in data:
            java_code = data['code']

            return jsonify(unit_test_generate(java_code))
        else:
            return jsonify({"error": "Payload中未包含'code'字段"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(debug=True)
