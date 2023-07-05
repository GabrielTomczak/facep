from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5173"]}})

@app.route('/face_analysis', methods=['GET'])
def face_analysis():
  name = request.args.get('name')
  sex = request.args.get('sex')
  result = subprocess.run(['python', './faceAnalysis.py', name, sex], capture_output=True, text=True)
  if result.returncode == 0:
    return result.stdout
  else:
    return "Falha ao realizar análise facial."

if __name__ == '__main__':
  app.run()