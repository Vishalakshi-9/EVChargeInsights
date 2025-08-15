"""
Report Generator for EV Charging Industry Analysis
Generates professional HTML and Markdown reports
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any
from jinja2 import Template

class ReportGenerator:
    """Generates professional consulting-style reports"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def generate_html_report(self, data: Dict[str, Any]) -> str:
        """Generate comprehensive HTML report"""
        self.logger.info("Generating HTML report")
        
        template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EV Charging Industry Analysis - Strategic Consulting Report</title>
    <link rel="stylesheet" href="static/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="report-header">
            <div class="header-content">
                <h1><i class="fas fa-charging-station"></i> EV Charging Industry Analysis</h1>
                <h2>Strategic Market Assessment & Competitive Intelligence</h2>
                <div class="header-meta">
                    <p><i class="fas fa-calendar"></i> {{ metadata.generated_date }}</p>
                    <p><i class="fas fa-clock"></i> Generated at {{ metadata.generated_time }}</p>
                    <p><i class="fas fa-tag"></i> Version {{ metadata.report_version }}</p>
                </div>
            </div>
        </header>

        <!-- Executive Summary -->
        <section class="executive-summary">
            <h2><i class="fas fa-chart-line"></i> Executive Summary</h2>
            <div class="summary-grid">
                <div class="summary-card">
                    <h3>Market Value</h3>
                    <div class="metric">${{ market_sizing.current_market.global_value_billion }}B</div>
                    <p>Global EV charging market</p>
                </div>
                <div class="summary-card">
                    <h3>Growth Rate</h3>
                    <div class="metric">{{ market_sizing.current_market.annual_growth_rate }}%</div>
                    <p>Annual growth projected</p>
                </div>
                <div class="summary-card">
                    <h3>Market Leader</h3>
                    <div class="metric">{{ competitive_analysis.top_players[0] }}</div>
                    <p>Dominant market position</p>
                </div>
                <div class="summary-card">
                    <h3>Industry Outlook</h3>
                    <div class="metric">{{ porters_analysis.overall_assessment.attractiveness }}</div>
                    <p>Porter's assessment</p>
                </div>
            </div>
            
            <div class="key-findings">
                <h3>Key Findings</h3>
                <ul>
                    <li>The EV charging market is experiencing unprecedented growth driven by government mandates and declining EV costs</li>
                    <li>Tesla maintains technological leadership but faces intensifying competition from network operators</li>
                    <li>Market fragmentation creates opportunities for consolidation and strategic partnerships</li>
                    <li>Rural market penetration remains a significant growth opportunity with infrastructure challenges</li>
                </ul>
            </div>
        </section>

        <!-- Industry Overview -->
        <section class="industry-overview">
            <h2><i class="fas fa-industry"></i> Industry Overview</h2>
            
            <div class="overview-content">
                <div class="market-trends">
                    <h3>Market Trends</h3>
                    <ul>
                        {% for trend in industry_overview.market_trends %}
                        <li>{{ trend }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="growth-drivers">
                    <h3>Growth Drivers</h3>
                    <ul>
                        {% for driver in industry_overview.growth_drivers %}
                        <li>{{ driver }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="challenges">
                    <h3>Industry Challenges</h3>
                    <ul>
                        {% for challenge in industry_overview.industry_challenges %}
                        <li>{{ challenge }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            
            <div class="market-projection">
                <h3>Market Growth Projection</h3>
                <canvas id="marketGrowthChart"></canvas>
            </div>
        </section>

        <!-- Competitive Landscape -->
        <section class="competitive-landscape">
            <h2><i class="fas fa-chess"></i> Competitive Landscape</h2>
            
            <div class="competitor-analysis">
                <h3>Market Share Distribution</h3>
                <canvas id="marketShareChart"></canvas>
            </div>
            
            <div class="competitive-matrix">
                <h3>Competitive Analysis Matrix</h3>
                <table class="analysis-table">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Network Size</th>
                            <th>Charging Speed</th>
                            <th>Coverage</th>
                            <th>Innovation</th>
                            <th>Brand Strength</th>
                            <th>Financial Resources</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for company, scores in competitive_analysis.competitive_matrix.items() %}
                        <tr>
                            <td><strong>{{ company }}</strong></td>
                            <td>{{ '★' * scores.network_size }}{{ '☆' * (5 - scores.network_size) }}</td>
                            <td>{{ '★' * scores.charging_speed }}{{ '☆' * (5 - scores.charging_speed) }}</td>
                            <td>{{ '★' * scores.geographic_coverage }}{{ '☆' * (5 - scores.geographic_coverage) }}</td>
                            <td>{{ '★' * scores.technology_innovation }}{{ '☆' * (5 - scores.technology_innovation) }}</td>
                            <td>{{ '★' * scores.brand_strength }}{{ '☆' * (5 - scores.brand_strength) }}</td>
                            <td>{{ '★' * scores.financial_resources }}{{ '☆' * (5 - scores.financial_resources) }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            
            <div class="key-insights">
                <h3>Competitive Insights</h3>
                <ul>
                    {% for insight in competitive_analysis.key_insights %}
                    <li>{{ insight }}</li>
                    {% endfor %}
                </ul>
            </div>
        </section>

        <!-- Porter's Five Forces -->
        <section class="porters-analysis">
            <h2><i class="fas fa-shield-alt"></i> Porter's Five Forces Analysis</h2>
            
            <div class="forces-grid">
                <div class="force-card threat-new-entrants">
                    <h3>Threat of New Entrants</h3>
                    <div class="force-score">{{ porters_analysis.threat_of_new_entrants.score }}/5</div>
                    <p class="force-assessment">{{ porters_analysis.threat_of_new_entrants.assessment }}</p>
                    <ul class="force-factors">
                        {% for factor in porters_analysis.threat_of_new_entrants.factors %}
                        <li>{{ factor }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="force-card supplier-power">
                    <h3>Supplier Power</h3>
                    <div class="force-score">{{ porters_analysis.bargaining_power_suppliers.score }}/5</div>
                    <p class="force-assessment">{{ porters_analysis.bargaining_power_suppliers.assessment }}</p>
                    <ul class="force-factors">
                        {% for factor in porters_analysis.bargaining_power_suppliers.factors %}
                        <li>{{ factor }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="force-card buyer-power">
                    <h3>Buyer Power</h3>
                    <div class="force-score">{{ porters_analysis.bargaining_power_buyers.score }}/5</div>
                    <p class="force-assessment">{{ porters_analysis.bargaining_power_buyers.assessment }}</p>
                    <ul class="force-factors">
                        {% for factor in porters_analysis.bargaining_power_buyers.factors %}
                        <li>{{ factor }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="force-card threat-substitutes">
                    <h3>Threat of Substitutes</h3>
                    <div class="force-score">{{ porters_analysis.threat_of_substitutes.score }}/5</div>
                    <p class="force-assessment">{{ porters_analysis.threat_of_substitutes.assessment }}</p>
                    <ul class="force-factors">
                        {% for factor in porters_analysis.threat_of_substitutes.factors %}
                        <li>{{ factor }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="force-card competitive-rivalry">
                    <h3>Competitive Rivalry</h3>
                    <div class="force-score">{{ porters_analysis.competitive_rivalry.score }}/5</div>
                    <p class="force-assessment">{{ porters_analysis.competitive_rivalry.assessment }}</p>
                    <ul class="force-factors">
                        {% for factor in porters_analysis.competitive_rivalry.factors %}
                        <li>{{ factor }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            
            <div class="overall-assessment">
                <h3>Overall Industry Assessment</h3>
                <p><strong>Industry Attractiveness:</strong> {{ porters_analysis.overall_assessment.attractiveness }}</p>
                <div class="recommendations">
                    <h4>Strategic Recommendations:</h4>
                    <ul>
                        {% for rec in porters_analysis.overall_assessment.key_recommendations %}
                        <li>{{ rec }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </section>

        <!-- SWOT Analysis -->
        <section class="swot-analysis">
            <h2><i class="fas fa-crosshairs"></i> SWOT Analysis</h2>
            
            <div class="swot-grid">
                <div class="swot-quadrant strengths">
                    <h3><i class="fas fa-thumbs-up"></i> Strengths</h3>
                    <ul>
                        {% for strength in swot_analysis.strengths %}
                        <li>{{ strength }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="swot-quadrant weaknesses">
                    <h3><i class="fas fa-exclamation-triangle"></i> Weaknesses</h3>
                    <ul>
                        {% for weakness in swot_analysis.weaknesses %}
                        <li>{{ weakness }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="swot-quadrant opportunities">
                    <h3><i class="fas fa-rocket"></i> Opportunities</h3>
                    <ul>
                        {% for opportunity in swot_analysis.opportunities %}
                        <li>{{ opportunity }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="swot-quadrant threats">
                    <h3><i class="fas fa-skull-crossbones"></i> Threats</h3>
                    <ul>
                        {% for threat in swot_analysis.threats %}
                        <li>{{ threat }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            
            <div class="strategic-options">
                <h3>Strategic Options</h3>
                <div class="strategies-grid">
                    <div class="strategy-card">
                        <h4>SO Strategies (Strengths + Opportunities)</h4>
                        <ul>
                            {% for strategy in swot_analysis.strategic_options.SO_strategies %}
                            <li>{{ strategy }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="strategy-card">
                        <h4>WO Strategies (Weaknesses + Opportunities)</h4>
                        <ul>
                            {% for strategy in swot_analysis.strategic_options.WO_strategies %}
                            <li>{{ strategy }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="strategy-card">
                        <h4>ST Strategies (Strengths + Threats)</h4>
                        <ul>
                            {% for strategy in swot_analysis.strategic_options.ST_strategies %}
                            <li>{{ strategy }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="strategy-card">
                        <h4>WT Strategies (Weaknesses + Threats)</h4>
                        <ul>
                            {% for strategy in swot_analysis.strategic_options.WT_strategies %}
                            <li>{{ strategy }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Market Sizing -->
        <section class="market-sizing">
            <h2><i class="fas fa-chart-pie"></i> Market Sizing & Projections</h2>
            
            <div class="sizing-overview">
                <div class="tam-sam-som">
                    <div class="market-tier">
                        <h3>TAM</h3>
                        <div class="market-value">${{ market_sizing.addressable_market.tam_billion }}B</div>
                        <p>Total Addressable Market</p>
                    </div>
                    <div class="market-tier">
                        <h3>SAM</h3>
                        <div class="market-value">${{ market_sizing.addressable_market.sam_billion }}B</div>
                        <p>Serviceable Addressable Market</p>
                    </div>
                    <div class="market-tier">
                        <h3>SOM</h3>
                        <div class="market-value">${{ market_sizing.addressable_market.som_billion }}B</div>
                        <p>Serviceable Obtainable Market</p>
                    </div>
                </div>
            </div>
            
            <div class="regional-analysis">
                <h3>Regional Market Distribution</h3>
                <canvas id="regionalChart"></canvas>
            </div>
            
            <div class="market-drivers">
                <h3>Key Market Drivers</h3>
                <ul>
                    {% for driver in market_sizing.market_drivers %}
                    <li>{{ driver }}</li>
                    {% endfor %}
                </ul>
            </div>
        </section>

        <!-- Trends & Future Outlook -->
        <section class="trends-analysis">
            <h2><i class="fas fa-crystal-ball"></i> Industry Trends & Future Outlook</h2>
            
            <div class="trends-grid">
                <div class="trend-category">
                    <h3>Technology Trends</h3>
                    <ul>
                        {% for trend in trend_analysis.technology_trends %}
                        <li>{{ trend }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="trend-category">
                    <h3>Market Trends</h3>
                    <ul>
                        {% for trend in trend_analysis.market_trends %}
                        <li>{{ trend }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="trend-category">
                    <h3>Business Model Trends</h3>
                    <ul>
                        {% for trend in trend_analysis.business_model_trends %}
                        <li>{{ trend }}</li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="trend-category">
                    <h3>Regulatory Trends</h3>
                    <ul>
                        {% for trend in trend_analysis.regulatory_trends %}
                        <li>{{ trend }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            
            <div class="outlook">
                <h3>2025-2030 Outlook</h3>
                <div class="outlook-grid">
                    <div class="outlook-item">
                        <h4>Market Maturity</h4>
                        <p>{{ trend_analysis.outlook_2025_2030.market_maturity }}</p>
                    </div>
                    <div class="outlook-item">
                        <h4>Competition Level</h4>
                        <p>{{ trend_analysis.outlook_2025_2030.competition_level }}</p>
                    </div>
                    <div class="outlook-item">
                        <h4>Technology Focus</h4>
                        <p>{{ trend_analysis.outlook_2025_2030.technology_focus }}</p>
                    </div>
                </div>
                
                <h4>Key Success Factors</h4>
                <ul>
                    {% for factor in trend_analysis.outlook_2025_2030.key_success_factors %}
                    <li>{{ factor }}</li>
                    {% endfor %}
                </ul>
            </div>
        </section>

        <!-- Strategic Recommendations -->
        <section class="recommendations">
            <h2><i class="fas fa-lightbulb"></i> Strategic Recommendations</h2>
            
            <div class="recommendations-content">
                <div class="recommendation-tier">
                    <h3>Immediate Actions (0-6 months)</h3>
                    <ul>
                        <li>Secure prime locations in high-traffic corridors</li>
                        <li>Establish partnerships with major fleet operators</li>
                        <li>Invest in ultra-fast charging technology deployment</li>
                        <li>Develop comprehensive customer experience strategy</li>
                    </ul>
                </div>
                
                <div class="recommendation-tier">
                    <h3>Short-term Initiatives (6-18 months)</h3>
                    <ul>
                        <li>Expand network density in target metropolitan areas</li>
                        <li>Launch subscription-based pricing models</li>
                        <li>Integrate renewable energy sources at charging sites</li>
                        <li>Develop strategic partnerships with utilities</li>
                    </ul>
                </div>
                
                <div class="recommendation-tier">
                    <h3>Long-term Strategy (18+ months)</h3>
                    <ul>
                        <li>Pursue consolidation opportunities in fragmented markets</li>
                        <li>Expand internationally in emerging EV markets</li>
                        <li>Develop adjacent service offerings (retail, advertising)</li>
                        <li>Invest in next-generation charging technologies</li>
                    </ul>
                </div>
            </div>
            
            <div class="success-metrics">
                <h3>Success Metrics to Track</h3>
                <ul>
                    <li>Network utilization rates and revenue per station</li>
                    <li>Customer acquisition cost and lifetime value</li>
                    <li>Market share in target geographic regions</li>
                    <li>Technology differentiation and charging speeds</li>
                    <li>Partnership development and strategic alliances</li>
                </ul>
            </div>
        </section>

        <!-- Footer -->
        <footer class="report-footer">
            <div class="footer-content">
                <p><i class="fas fa-info-circle"></i> This report is based on publicly available data and industry analysis as of {{ metadata.generated_date }}.</p>
                <p><i class="fas fa-chart-bar"></i> Data sources include industry websites, market reports, and competitive intelligence.</p>
                <p><i class="fas fa-code"></i> Generated by EV Charging Industry Analysis Tool v{{ metadata.report_version }}</p>
            </div>
        </footer>
    </div>

    <script>
        // Market Growth Chart
        const growthCtx = document.getElementById('marketGrowthChart').getContext('2d');
        new Chart(growthCtx, {
            type: 'line',
            data: {
                labels: {{ growth_chart_labels | safe }},
                datasets: [{
                    label: 'Market Value (Billion USD)',
                    data: {{ growth_chart_data | safe }},
                    borderColor: '#2E8B57',
                    backgroundColor: 'rgba(46, 139, 87, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Market Value (Billion USD)'
                        }
                    }
                }
            }
        });

        // Market Share Chart
        const shareCtx = document.getElementById('marketShareChart').getContext('2d');
        new Chart(shareCtx, {
            type: 'doughnut',
            data: {
                labels: {{ market_share_labels | safe }},
                datasets: [{
                    data: {{ market_share_data | safe }},
                    backgroundColor: ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });

        // Regional Distribution Chart
        const regionalCtx = document.getElementById('regionalChart').getContext('2d');
        new Chart(regionalCtx, {
            type: 'bar',
            data: {
                labels: {{ regional_labels | safe }},
                datasets: [{
                    label: 'Market Share (%)',
                    data: {{ regional_data | safe }},
                    backgroundColor: ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Market Share (%)'
                        }
                    }
                }
            }
        });
    </script>
</body>
</html>
        """)
        
        # Prepare chart data
        market_sizing = data.get('market_sizing', {})
        projections = market_sizing.get('projections', {})
        current_value = market_sizing.get('current_market', {}).get('global_value_billion', 15.2)
        
        growth_labels = json.dumps(['2024'] + list(projections.keys()))
        growth_data = json.dumps([current_value] + list(projections.values()))
        
        competitive_analysis = data.get('competitive_analysis', {})
        market_share = competitive_analysis.get('market_share_estimates', {})
        share_labels = json.dumps(list(market_share.keys()))
        share_data = json.dumps(list(market_share.values()))
        
        regional_data = market_sizing.get('regional_analysis', {})
        regional_labels = json.dumps(list(regional_data.keys()))
        regional_values = json.dumps(list(regional_data.values()))
        
        # Extract nested data for template rendering
        template_data = {
            'metadata': data.get('metadata', {}),
            'industry_overview': data.get('industry_data', {}).get('industry_overview', {}),
            'competitive_analysis': data.get('competitive_analysis', {}),
            'porters_analysis': data.get('porters_analysis', {}),
            'swot_analysis': data.get('swot_analysis', {}),
            'market_sizing': data.get('market_sizing', {}),
            'trend_analysis': data.get('trend_analysis', {}),
            'growth_chart_labels': growth_labels,
            'growth_chart_data': growth_data,
            'market_share_labels': share_labels,
            'market_share_data': share_data,
            'regional_labels': regional_labels,
            'regional_data': regional_values
        }
        
        return template.render(**template_data)
    
    def generate_markdown_report(self, data: Dict[str, Any]) -> str:
        """Generate Markdown version of the report"""
        self.logger.info("Generating Markdown report")
        
        metadata = data.get('metadata', {})
        market_sizing = data.get('market_sizing', {})
        competitive_analysis = data.get('competitive_analysis', {})
        porters_analysis = data.get('porters_analysis', {})
        swot_analysis = data.get('swot_analysis', {})
        trend_analysis = data.get('trend_analysis', {})
        
        markdown_content = f"""# EV Charging Industry Analysis
## Strategic Market Assessment & Competitive Intelligence

**Generated:** {metadata.get('generated_date', 'N/A')} at {metadata.get('generated_time', 'N/A')}  
**Version:** {metadata.get('report_version', 'N/A')}

---

## Executive Summary

### Key Metrics
- **Global Market Value:** ${market_sizing.get('current_market', {}).get('global_value_billion', 'N/A')}B
- **Annual Growth Rate:** {market_sizing.get('current_market', {}).get('annual_growth_rate', 'N/A')}%
- **Market Leader:** {competitive_analysis.get('top_players', ['N/A'])[0] if competitive_analysis.get('top_players') else 'N/A'}
- **Industry Attractiveness:** {porters_analysis.get('overall_assessment', {}).get('attractiveness', 'N/A')}

### Key Findings
- The EV charging market is experiencing unprecedented growth driven by government mandates and declining EV costs
- Tesla maintains technological leadership but faces intensifying competition from network operators  
- Market fragmentation creates opportunities for consolidation and strategic partnerships
- Rural market penetration remains a significant growth opportunity with infrastructure challenges

---

## Industry Overview

### Market Trends
"""
        
        industry_overview = data.get('industry_overview', {})
        for trend in industry_overview.get('market_trends', []):
            markdown_content += f"- {trend}\n"
        
        markdown_content += """
### Growth Drivers
"""
        for driver in industry_overview.get('growth_drivers', []):
            markdown_content += f"- {driver}\n"
        
        markdown_content += """
### Industry Challenges
"""
        for challenge in industry_overview.get('industry_challenges', []):
            markdown_content += f"- {challenge}\n"
        
        markdown_content += f"""
---

## Competitive Landscape

### Market Share Distribution
"""
        market_share = competitive_analysis.get('market_share_estimates', {})
        for company, share in market_share.items():
            markdown_content += f"- **{company}:** {share}%\n"
        
        markdown_content += """
### Competitive Analysis Matrix

| Company | Network Size | Charging Speed | Coverage | Innovation | Brand | Financial |
|---------|-------------|---------------|----------|------------|-------|-----------|
"""
        
        matrix = competitive_analysis.get('competitive_matrix', {})
        for company, scores in matrix.items():
            markdown_content += f"| {company} | {scores.get('network_size', 0)}/5 | {scores.get('charging_speed', 0)}/5 | {scores.get('geographic_coverage', 0)}/5 | {scores.get('technology_innovation', 0)}/5 | {scores.get('brand_strength', 0)}/5 | {scores.get('financial_resources', 0)}/5 |\n"
        
        markdown_content += f"""
---

## Porter's Five Forces Analysis

### Threat of New Entrants: {porters_analysis.get('threat_of_new_entrants', {}).get('score', 0)}/5
**Assessment:** {porters_analysis.get('threat_of_new_entrants', {}).get('assessment', 'N/A')}

Key Factors:
"""
        for factor in porters_analysis.get('threat_of_new_entrants', {}).get('factors', []):
            markdown_content += f"- {factor}\n"
        
        markdown_content += f"""
### Bargaining Power of Suppliers: {porters_analysis.get('bargaining_power_suppliers', {}).get('score', 0)}/5
**Assessment:** {porters_analysis.get('bargaining_power_suppliers', {}).get('assessment', 'N/A')}

Key Factors:
"""
        for factor in porters_analysis.get('bargaining_power_suppliers', {}).get('factors', []):
            markdown_content += f"- {factor}\n"
        
        markdown_content += f"""
### Bargaining Power of Buyers: {porters_analysis.get('bargaining_power_buyers', {}).get('score', 0)}/5
**Assessment:** {porters_analysis.get('bargaining_power_buyers', {}).get('assessment', 'N/A')}

Key Factors:
"""
        for factor in porters_analysis.get('bargaining_power_buyers', {}).get('factors', []):
            markdown_content += f"- {factor}\n"
        
        markdown_content += f"""
### Threat of Substitutes: {porters_analysis.get('threat_of_substitutes', {}).get('score', 0)}/5
**Assessment:** {porters_analysis.get('threat_of_substitutes', {}).get('assessment', 'N/A')}

Key Factors:
"""
        for factor in porters_analysis.get('threat_of_substitutes', {}).get('factors', []):
            markdown_content += f"- {factor}\n"
        
        markdown_content += f"""
### Competitive Rivalry: {porters_analysis.get('competitive_rivalry', {}).get('score', 0)}/5
**Assessment:** {porters_analysis.get('competitive_rivalry', {}).get('assessment', 'N/A')}

Key Factors:
"""
        for factor in porters_analysis.get('competitive_rivalry', {}).get('factors', []):
            markdown_content += f"- {factor}\n"
        
        markdown_content += f"""
### Overall Industry Assessment
**Industry Attractiveness:** {porters_analysis.get('overall_assessment', {}).get('attractiveness', 'N/A')}

**Strategic Recommendations:**
"""
        for rec in porters_analysis.get('overall_assessment', {}).get('key_recommendations', []):
            markdown_content += f"- {rec}\n"
        
        markdown_content += f"""
---

## SWOT Analysis

### Strengths
"""
        for strength in swot_analysis.get('strengths', []):
            markdown_content += f"- {strength}\n"
        
        markdown_content += """
### Weaknesses
"""
        for weakness in swot_analysis.get('weaknesses', []):
            markdown_content += f"- {weakness}\n"
        
        markdown_content += """
### Opportunities
"""
        for opportunity in swot_analysis.get('opportunities', []):
            markdown_content += f"- {opportunity}\n"
        
        markdown_content += """
### Threats
"""
        for threat in swot_analysis.get('threats', []):
            markdown_content += f"- {threat}\n"
        
        markdown_content += f"""
---

## Market Sizing & Projections

### Addressable Market
- **TAM (Total Addressable Market):** ${market_sizing.get('addressable_market', {}).get('tam_billion', 'N/A')}B
- **SAM (Serviceable Addressable Market):** ${market_sizing.get('addressable_market', {}).get('sam_billion', 'N/A')}B  
- **SOM (Serviceable Obtainable Market):** ${market_sizing.get('addressable_market', {}).get('som_billion', 'N/A')}B

### Regional Distribution
"""
        regional_analysis = market_sizing.get('regional_analysis', {})
        for region, percentage in regional_analysis.items():
            markdown_content += f"- **{region}:** {percentage}%\n"
        
        markdown_content += """
### Market Projections
"""
        projections = market_sizing.get('projections', {})
        for year, value in projections.items():
            markdown_content += f"- **{year}:** ${value}B\n"
        
        markdown_content += f"""
---

## Industry Trends & Future Outlook

### Technology Trends
"""
        for trend in trend_analysis.get('technology_trends', []):
            markdown_content += f"- {trend}\n"
        
        markdown_content += """
### Market Trends
"""
        for trend in trend_analysis.get('market_trends', []):
            markdown_content += f"- {trend}\n"
        
        markdown_content += """
### Business Model Trends
"""
        for trend in trend_analysis.get('business_model_trends', []):
            markdown_content += f"- {trend}\n"
        
        markdown_content += """
### Regulatory Trends
"""
        for trend in trend_analysis.get('regulatory_trends', []):
            markdown_content += f"- {trend}\n"
        
        outlook = trend_analysis.get('outlook_2025_2030', {})
        markdown_content += f"""
### 2025-2030 Outlook
- **Market Maturity:** {outlook.get('market_maturity', 'N/A')}
- **Competition Level:** {outlook.get('competition_level', 'N/A')}
- **Technology Focus:** {outlook.get('technology_focus', 'N/A')}

**Key Success Factors:**
"""
        for factor in outlook.get('key_success_factors', []):
            markdown_content += f"- {factor}\n"
        
        markdown_content += """
---

## Strategic Recommendations

### Immediate Actions (0-6 months)
- Secure prime locations in high-traffic corridors
- Establish partnerships with major fleet operators  
- Invest in ultra-fast charging technology deployment
- Develop comprehensive customer experience strategy

### Short-term Initiatives (6-18 months)
- Expand network density in target metropolitan areas
- Launch subscription-based pricing models
- Integrate renewable energy sources at charging sites
- Develop strategic partnerships with utilities

### Long-term Strategy (18+ months)
- Pursue consolidation opportunities in fragmented markets
- Expand internationally in emerging EV markets
- Develop adjacent service offerings (retail, advertising)
- Invest in next-generation charging technologies

### Success Metrics to Track
- Network utilization rates and revenue per station
- Customer acquisition cost and lifetime value
- Market share in target geographic regions
- Technology differentiation and charging speeds
- Partnership development and strategic alliances

---

*This report is based on publicly available data and industry analysis as of {metadata.get('generated_date', 'N/A')}.*

*Generated by EV Charging Industry Analysis Tool v{metadata.get('report_version', 'N/A')}*
"""
        
        return markdown_content
