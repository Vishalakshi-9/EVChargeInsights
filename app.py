"""
Production Flask app for EV Charging Industry Analysis
Optimized for Render deployment
"""

from flask import Flask, send_file, jsonify, send_from_directory
import os
import json
import subprocess
import threading
from datetime import datetime

app = Flask(__name__)

# Ensure reports are generated on startup
def generate_reports_if_missing():
    """Generate reports if they don't exist"""
    if not os.path.exists('ev_charging_analysis_report.html'):
        try:
            print("🚗⚡ Generating initial reports...")
            subprocess.run(['python', 'main.py'], check=True, capture_output=True, text=True)
            print("✅ Reports generated successfully")
        except Exception as e:
            print(f"❌ Error generating reports: {e}")

# Generate reports on startup in background
threading.Thread(target=generate_reports_if_missing, daemon=True).start()

@app.route('/')
def index():
    """Serve the main analysis report"""
    try:
        if os.path.exists('ev_charging_analysis_report.html'):
            return send_file('ev_charging_analysis_report.html')
        else:
            return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>EV Charging Industry Analysis</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body { font-family: Arial, sans-serif; padding: 40px; text-align: center; background: #f8f9fa; }
                    .container { max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                    h1 { color: #2E8B57; margin-bottom: 20px; }
                    .loading { color: #666; margin: 20px 0; }
                    .button { background: #2E8B57; color: white; padding: 12px 24px; border: none; border-radius: 5px; text-decoration: none; display: inline-block; margin: 10px; }
                    .button:hover { background: #1e5f3f; }
                    pre { background: #f5f5f5; padding: 20px; border-radius: 8px; text-align: left; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🚗⚡ EV Charging Industry Analysis</h1>
                    <div class="loading">
                        <p>📊 Reports are being generated in the background...</p>
                        <p>This may take 30-60 seconds for the first load.</p>
                    </div>
                    <a href="/generate" class="button">🔄 Generate Report</a>
                    <a href="/status" class="button">📈 Check Status</a>
                    <br><br>
                    <p><small>Refresh this page in a few moments to view the completed report.</small></p>
                </div>
                <script>
                    // Auto-refresh every 10 seconds if no report is available
                    setTimeout(function() { window.location.reload(); }, 10000);
                </script>
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
            return jsonify({"error": "Analysis data not found. Report is being generated."})
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
    def run_analysis():
        try:
            subprocess.run(['python', 'main.py'], check=True, capture_output=True, text=True)
            print("✅ Analysis completed successfully")
        except Exception as e:
            print(f"❌ Error running analysis: {e}")
    
    # Run analysis in background
    thread = threading.Thread(target=run_analysis)
    thread.start()
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generating EV Analysis Report</title>
        <meta http-equiv="refresh" content="30;url=/">
        <style>
            body { font-family: Arial, sans-serif; padding: 40px; text-align: center; background: #f8f9fa; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2E8B57; }
            .spinner { border: 4px solid #f3f3f3; border-top: 4px solid #2E8B57; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 20px auto; }
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            .button { background: #2E8B57; color: white; padding: 12px 24px; border: none; border-radius: 5px; text-decoration: none; display: inline-block; margin: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚗⚡ Generating EV Charging Analysis</h1>
            <div class="spinner"></div>
            <p>The comprehensive industry analysis is running...</p>
            <p>This includes data collection, competitive analysis, Porter's Five Forces, SWOT analysis, and market sizing.</p>
            <p>This page will automatically refresh in 30 seconds.</p>
            <a href="/" class="button">🔄 Check Report</a>
        </div>
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
        'last_generated': datetime.fromtimestamp(os.path.getmtime('ev_charging_analysis_report.html')).isoformat() if os.path.exists('ev_charging_analysis_report.html') else None,
        'server_status': 'running',
        'environment': 'production'
    }
    
    return jsonify(files_status)

@app.route('/health')
def health():
    """Health check endpoint for Render"""
    return jsonify({'status': 'healthy', 'service': 'ev-charging-analysis'})

if __name__ == '__main__':
    # Use environment port or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    print("🚗⚡ Starting EV Charging Analysis Web Server (Production)")
    print(f"📊 Server running on port {port}")
    
    # Production configuration
    app.run(host='0.0.0.0', port=port, debug=False)