"""
Simple web server to display the generated EV charging industry analysis report
"""

from flask import Flask, send_file, render_template_string, jsonify, send_from_directory
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main analysis report"""
    try:
        if os.path.exists('ev_charging_analysis_report.html'):
            return send_file('ev_charging_analysis_report.html')
        else:
            return """
            <html>
            <head><title>EV Charging Analysis</title></head>
            <body style="font-family: Arial, sans-serif; padding: 40px; text-align: center;">
                <h1>🚗⚡ EV Charging Industry Analysis</h1>
                <p>Report not yet generated. Please run the analysis first:</p>
                <pre style="background: #f5f5f5; padding: 20px; border-radius: 8px; text-align: left; max-width: 400px; margin: 20px auto;">python main.py</pre>
                <p>Once generated, refresh this page to view the report.</p>
            </body>
            </html>
            """
    except Exception as e:
        return f"Error loading report: {str(e)}"

@app.route('/report')
def report():
    """Alternative route for the main report"""
    return index()

@app.route('/data')
def data():
    """Serve the raw analysis data as JSON"""
    try:
        if os.path.exists('analysis_data.json'):
            with open('analysis_data.json', 'r') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify({"error": "Analysis data not found. Run the analysis first."})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/visualizations/<filename>')
def visualizations(filename):
    """Serve visualization images"""
    try:
        return send_file(filename)
    except:
        return "Visualization not found", 404

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

@app.route('/generate')
def generate():
    """Endpoint to trigger report generation"""
    import subprocess
    import threading
    
    def run_analysis():
        try:
            subprocess.run(['python', 'main.py'], check=True, capture_output=True, text=True)
        except Exception as e:
            print(f"Error running analysis: {e}")
    
    # Run analysis in background
    thread = threading.Thread(target=run_analysis)
    thread.start()
    
    return """
    <html>
    <head>
        <title>Generating Report</title>
        <meta http-equiv="refresh" content="30;url=/">
    </head>
    <body style="font-family: Arial, sans-serif; padding: 40px; text-align: center;">
        <h1>🚗⚡ Generating EV Charging Analysis</h1>
        <p>The analysis is running in the background...</p>
        <p>This page will automatically refresh in 30 seconds.</p>
        <p><a href="/">Check Report</a></p>
    </body>
    </html>
    """

@app.route('/status')
def status():
    """Check the status of generated files"""
    files_status = {
        'html_report': os.path.exists('ev_charging_analysis_report.html'),
        'markdown_report': os.path.exists('ev_charging_analysis_report.md'),
        'analysis_data': os.path.exists('analysis_data.json'),
        'visualizations': {
            'market_growth': os.path.exists('market_growth_projection.png'),
            'competitive_radar': os.path.exists('competitive_analysis_radar.png'),
            'market_share': os.path.exists('market_share_distribution.png'),
            'regional_distribution': os.path.exists('regional_market_distribution.png')
        },
        'last_generated': datetime.fromtimestamp(os.path.getmtime('ev_charging_analysis_report.html')).isoformat() if os.path.exists('ev_charging_analysis_report.html') else None
    }
    
    return jsonify(files_status)

if __name__ == '__main__':
    print("🚗⚡ Starting EV Charging Analysis Web Server")
    print("📊 View report at: http://localhost:5000")
    print("📋 Raw data at: http://localhost:5000/data") 
    print("🔄 Generate new report: http://localhost:5000/generate")
    print("📈 Status check: http://localhost:5000/status")
    app.run(host='0.0.0.0', port=5000, debug=True)