import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        return jsonify(member), 200
    except ValueError as e:
        return str(e), 400

@app.route('/member', methods=['POST'])
def add_member():
    try:
        member_data = request.get_json()
        if member_data:
            jackson_family.add_member(member_data)
            return jsonify(member_data), 200
        else:
            return "Invalid member data", 400
    except ValueError as e:
        return str(e), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    except ValueError as e:
        return str(e), 400 

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
