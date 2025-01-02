from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize an empty queue
queue = []

@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.json
    element = data.get('element')
    queue.append(element)
    return jsonify({"message": f"Enqueued {element}", "queue": queue})

@app.route('/dequeue', methods=['POST'])
def dequeue():
    if queue:
        removed = queue.pop(0)
        return jsonify({"message": f"Dequeued {removed}", "queue": queue})
    return jsonify({"error": "Queue is empty"}), 400

@app.route('/peek', methods=['GET'])
def peek():
    if queue:
        return jsonify({"front": queue[0]})
    return jsonify({"error": "Queue is empty"}), 400

@app.route('/queue', methods=['GET'])
def get_queue():
    return jsonify({"queue": queue})

if __name__ == '__main__':
    app.run(debug=True)
