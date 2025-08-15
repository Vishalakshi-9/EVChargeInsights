"""
Utility functions for EV Charging Industry Analysis
"""

import os
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('ev_analysis.log'),
            logging.StreamHandler()
        ]
    )

def create_directories():
    """Create necessary directories for the project"""
    directories = [
        'static',
        'templates', 
        'data',
        'exports',
        'visualizations'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")

def format_currency(amount: float) -> str:
    """Format number as currency"""
    if amount >= 1000000000:
        return f"${amount/1000000000:.1f}B"
    elif amount >= 1000000:
        return f"${amount/1000000:.1f}M"
    elif amount >= 1000:
        return f"${amount/1000:.1f}K"
    else:
        return f"${amount:.0f}"

def calculate_growth_rate(start_value: float, end_value: float, periods: int) -> float:
    """Calculate compound annual growth rate"""
    if start_value <= 0 or end_value <= 0 or periods <= 0:
        return 0.0
    
    return ((end_value / start_value) ** (1 / periods) - 1) * 100

def validate_data_quality(data: Dict) -> Dict[str, Any]:
    """Validate the quality of collected data"""
    quality_report = {
        'completeness_score': 0,
        'data_sources_count': 0,
        'missing_fields': [],
        'quality_rating': 'Poor'
    }
    
    # Check for required fields
    required_fields = [
        'competitors',
        'industry_overview', 
        'market_sizing'
    ]
    
    present_fields = 0
    for field in required_fields:
        if field in data and data[field]:
            present_fields += 1
        else:
            quality_report['missing_fields'].append(field)
    
    # Calculate completeness score
    quality_report['completeness_score'] = (present_fields / len(required_fields)) * 100
    
    # Count data sources
    if 'collection_metadata' in data:
        quality_report['data_sources_count'] = data['collection_metadata'].get('sources_accessed', 0)
    
    # Determine quality rating
    if quality_report['completeness_score'] >= 80:
        quality_report['quality_rating'] = 'Excellent'
    elif quality_report['completeness_score'] >= 60:
        quality_report['quality_rating'] = 'Good'
    elif quality_report['completeness_score'] >= 40:
        quality_report['quality_rating'] = 'Fair'
    else:
        quality_report['quality_rating'] = 'Poor'
    
    return quality_report

def generate_executive_summary(data: Dict) -> str:
    """Generate executive summary text"""
    market_size = data.get('market_sizing', {}).get('current_market', {}).get('global_value_billion', 'N/A')
    growth_rate = data.get('market_sizing', {}).get('current_market', {}).get('annual_growth_rate', 'N/A')
    top_player = data.get('competitive_analysis', {}).get('top_players', ['N/A'])[0] if data.get('competitive_analysis', {}).get('top_players') else 'N/A'
    
    summary = f"""
    The global EV charging market is valued at ${market_size}B with an annual growth rate of {growth_rate}%.
    {top_player} currently leads the market through technological innovation and network effects.
    The industry shows high growth potential driven by government mandates and declining EV costs.
    Market fragmentation presents consolidation opportunities for strategic players.
    """
    
    return summary.strip()

def safe_get(dictionary: Dict, keys: List[str], default=None):
    """Safely get nested dictionary values"""
    for key in keys:
        try:
            dictionary = dictionary[key]
        except (KeyError, TypeError):
            return default
    return dictionary

def format_percentage(value: float) -> str:
    """Format number as percentage"""
    return f"{value:.1f}%" if isinstance(value, (int, float)) else "N/A"

def clean_text_content(text: str, max_length: int = 5000) -> str:
    """Clean and truncate text content"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length] + "..."
    
    return text

def generate_timestamp() -> str:
    """Generate formatted timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

def export_data_to_json(data: Dict, filename: Optional[str] = None):
    """Export data to JSON file"""
    import json
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ev_analysis_data_{timestamp}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)
        logging.info(f"Data exported to {filename}")
        return filename
    except Exception as e:
        logging.error(f"Error exporting data to JSON: {str(e)}")
        return None

def calculate_market_metrics(current_size: float, growth_rate: float, years: int) -> Dict[str, float]:
    """Calculate future market projections"""
    projections = {}
    
    for year in range(1, years + 1):
        future_value = current_size * ((1 + growth_rate / 100) ** year)
        projections[str(datetime.now().year + year)] = round(future_value, 1)
    
    return projections

def rank_by_score(items: Dict[str, Dict], score_key: str = 'total_score') -> List[str]:
    """Rank items by total score"""
    scores = {}
    
    for item, metrics in items.items():
        if isinstance(metrics, dict):
            if score_key in metrics:
                scores[item] = metrics[score_key]
            else:
                # Calculate total score from all numeric values
                total = sum(v for v in metrics.values() if isinstance(v, (int, float)))
                scores[item] = total
        else:
            scores[item] = 0
    
    return sorted(scores.keys(), key=lambda x: scores[x], reverse=True)

def create_data_summary(data: Dict) -> Dict[str, Any]:
    """Create a summary of collected data"""
    summary = {
        'timestamp': generate_timestamp(),
        'total_sections': len(data),
        'data_quality': validate_data_quality(data),
        'key_metrics': {}
    }
    
    # Extract key metrics
    market_sizing = data.get('market_sizing', {})
    if market_sizing:
        summary['key_metrics']['market_size'] = market_sizing.get('current_market', {}).get('global_value_billion')
        summary['key_metrics']['growth_rate'] = market_sizing.get('current_market', {}).get('annual_growth_rate')
    
    competitive_analysis = data.get('competitive_analysis', {})
    if competitive_analysis:
        summary['key_metrics']['competitors_analyzed'] = len(competitive_analysis.get('competitive_matrix', {}))
        summary['key_metrics']['market_leader'] = competitive_analysis.get('top_players', [None])[0]
    
    return summary
