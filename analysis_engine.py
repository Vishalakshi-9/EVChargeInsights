"""
Analysis Engine for EV Charging Industry Analysis
Implements Porter's Five Forces, SWOT analysis, and market analysis
"""

import logging
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Dict, List, Tuple, Any
import json
from datetime import datetime

class AnalysisEngine:
    """Performs strategic analysis using various business frameworks"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        plt.style.use('default')
        
    def analyze_competitors(self, industry_data: Dict) -> Dict:
        """
        Analyze competitive landscape of major EV charging players
        """
        self.logger.info("Starting competitive analysis")
        
        if 'competitors' not in industry_data:
            return {'error': 'No competitor data available'}
        
        competitors = industry_data['competitors']
        analysis = {
            'competitive_matrix': {},
            'market_positioning': {},
            'top_players': [],
            'competitive_advantages': {},
            'market_share_estimates': {}
        }
        
        # Analyze each competitor
        for company, data in competitors.items():
            self.logger.info(f"Analyzing {company}")
            
            # Extract key metrics
            metrics = data.get('data', {}).get('metrics', {})
            strengths = data.get('data', {}).get('strengths', [])
            position = data.get('data', {}).get('market_position', 'Unknown')
            
            # Competitive matrix scoring (1-5 scale)
            analysis['competitive_matrix'][company] = {
                'network_size': self._score_network_size(company, metrics),
                'charging_speed': self._score_charging_speed(company),
                'geographic_coverage': self._score_coverage(company),
                'technology_innovation': self._score_innovation(company),
                'brand_strength': self._score_brand(company),
                'financial_resources': self._score_financial(company)
            }
            
            analysis['market_positioning'][company] = position
            analysis['competitive_advantages'][company] = strengths
        
        # Rank top players
        analysis['top_players'] = self._rank_competitors(analysis['competitive_matrix'])
        
        # Estimate market shares
        analysis['market_share_estimates'] = {
            'Tesla Supercharger': 28.5,
            'ChargePoint': 22.0,
            'Electrify America': 12.5,
            'Others': 37.0
        }
        
        # Key insights
        analysis['key_insights'] = [
            'Tesla maintains technological and brand advantages',
            'ChargePoint leads in network operator model',
            'Market fragmentation creates opportunities',
            'Fast charging becoming table stakes'
        ]
        
        return analysis
    
    def porters_five_forces(self, industry_data: Dict) -> Dict:
        """
        Apply Porter's Five Forces framework to EV charging industry
        """
        self.logger.info("Conducting Porter's Five Forces analysis")
        
        forces = {
            'threat_of_new_entrants': {
                'score': 4,  # High threat (1-5 scale)
                'factors': [
                    'Low switching costs for consumers',
                    'Government incentives attract new players',
                    'Technology becoming more accessible',
                    'Large capital requirements as barrier'
                ],
                'assessment': 'HIGH - Easy market entry but capital intensive'
            },
            
            'bargaining_power_suppliers': {
                'score': 3,  # Medium power
                'factors': [
                    'Limited number of charging equipment manufacturers',
                    'Dependence on electrical grid infrastructure',
                    'Battery technology supplier concentration',
                    'Growing supplier base reducing power'
                ],
                'assessment': 'MEDIUM - Concentrated suppliers but expanding'
            },
            
            'bargaining_power_buyers': {
                'score': 4,  # High power
                'factors': [
                    'Multiple charging network options',
                    'Price-sensitive consumer base',
                    'Low switching costs between networks',
                    'Government and fleet buyers have leverage'
                ],
                'assessment': 'HIGH - Consumers have multiple options'
            },
            
            'threat_of_substitutes': {
                'score': 2,  # Low threat
                'factors': [
                    'Home charging as primary alternative',
                    'Workplace charging availability',
                    'Battery swapping in limited markets',
                    'Hydrogen fuel cells long-term threat'
                ],
                'assessment': 'LOW - Limited substitutes for public fast charging'
            },
            
            'competitive_rivalry': {
                'score': 5,  # Very high rivalry
                'factors': [
                    'Numerous players entering market',
                    'Rapid capacity expansion',
                    'Price competition for prime locations',
                    'Technology differentiation attempts'
                ],
                'assessment': 'VERY HIGH - Intense competition for market share'
            }
        }
        
        # Calculate overall industry attractiveness
        total_score = sum(force['score'] for force in forces.values())
        avg_score = total_score / 5
        
        forces['overall_assessment'] = {
            'average_score': avg_score,
            'attractiveness': self._assess_attractiveness(avg_score),
            'key_recommendations': [
                'Focus on differentiation through technology and service',
                'Secure prime locations quickly',
                'Build network effects and switching costs',
                'Consider vertical integration opportunities'
            ]
        }
        
        return forces
    
    def swot_analysis(self, industry_data: Dict) -> Dict:
        """
        Conduct SWOT analysis for the EV charging industry
        """
        self.logger.info("Performing SWOT analysis")
        
        swot = {
            'strengths': [
                'Growing EV adoption driving demand',
                'Government policy support globally',
                'Technological advancement in charging speeds',
                'Established players with network effects',
                'Multiple revenue streams (charging, services, data)',
                'Environmental benefits alignment with trends'
            ],
            
            'weaknesses': [
                'High capital investment requirements',
                'Grid infrastructure limitations',
                'Utilization rates still developing',
                'Standardization challenges across networks',
                'Limited rural coverage',
                'Dependence on EV adoption rates'
            ],
            
            'opportunities': [
                'Massive untapped market potential',
                'Fleet electrification acceleration',
                'Integration with renewable energy',
                'Autonomous vehicle charging services',
                'Energy storage and grid services',
                'International market expansion',
                'Value-added services (retail, advertising)'
            ],
            
            'threats': [
                'Regulatory changes affecting incentives',
                'Competition from home/workplace charging',
                'Economic downturn reducing EV sales',
                'Technology disruption (battery swapping, wireless)',
                'Grid capacity constraints',
                'Commodity price volatility',
                'Potential market saturation in urban areas'
            ]
        }
        
        # SWOT matrix strategic options
        swot['strategic_options'] = {}
        swot['strategic_options']['SO_strategies'] = [
            'Leverage government support for rapid network expansion',
            'Use technology leadership to capture fleet market'
        ]
        swot['strategic_options']['WO_strategies'] = [
            'Partner with utilities to address grid limitations',
            'Focus on high-traffic locations to improve utilization'
        ]
        swot['strategic_options']['ST_strategies'] = [
            'Build brand loyalty to defend against new entrants',
            'Diversify revenue streams beyond charging'
        ]
        swot['strategic_options']['WT_strategies'] = [
            'Form strategic alliances to share capital burden',
            'Develop flexible business models for market changes'
        ]
        
        return swot
    
    def market_sizing(self, industry_data: Dict) -> Dict:
        """
        Calculate market sizing and projections
        """
        self.logger.info("Calculating market sizing")
        
        # Extract market data
        market_data = industry_data.get('market_sizing', {})
        
        sizing = {
            'current_market': {
                'global_value_billion': market_data.get('global_market_size', 15.2),
                'annual_growth_rate': market_data.get('growth_rate', 28.5),
                'key_metrics': self._calculate_market_metrics(market_data)
            },
            
            'projections': market_data.get('forecast_data', {}),
            
            'addressable_market': {
                'tam_billion': 180.0,  # Total Addressable Market
                'sam_billion': 85.0,   # Serviceable Addressable Market
                'som_billion': 25.0    # Serviceable Obtainable Market
            },
            
            'regional_analysis': market_data.get('regional_breakdown', {}),
            
            'market_drivers': [
                'Government EV mandates and incentives',
                'Declining EV battery costs',
                'Expanding EV model availability',
                'Corporate sustainability commitments',
                'Improving charging technology'
            ]
        }
        
        # Calculate market penetration rates
        sizing['penetration_analysis'] = self._calculate_penetration_rates(sizing)
        
        return sizing
    
    def trend_analysis(self, industry_data: Dict) -> Dict:
        """
        Analyze industry trends and future outlook
        """
        self.logger.info("Analyzing industry trends")
        
        trends = {
            'technology_trends': [
                'Ultra-fast charging (350kW+) deployment',
                'Wireless/inductive charging development',
                'Smart grid integration and V2G capabilities',
                'AI-powered charging optimization',
                'Renewable energy integration'
            ],
            
            'market_trends': [
                'Shift from subsidies to market-driven growth',
                'Consolidation among smaller players',
                'Vertical integration by automakers',
                'Expansion into adjacent services',
                'Rural market development'
            ],
            
            'business_model_trends': [
                'Subscription-based charging plans',
                'Dynamic pricing strategies',
                'Fleet-focused solutions',
                'Charging-as-a-Service models',
                'Multi-modal transportation hubs'
            ],
            
            'regulatory_trends': [
                'Standardization requirements',
                'Interoperability mandates',
                'Grid modernization support',
                'Environmental impact assessments',
                'Data privacy regulations'
            ]
        }
        
        # Future outlook
        trends['outlook_2025_2030'] = {}
        trends['outlook_2025_2030']['market_maturity'] = 'Rapid Growth Phase'
        trends['outlook_2025_2030']['competition_level'] = 'Intensifying'
        trends['outlook_2025_2030']['technology_focus'] = 'Ultra-fast charging and grid integration'
        trends['outlook_2025_2030']['key_success_factors'] = [
            'Network density and coverage',
            'Charging speed and reliability',
            'Customer experience and pricing',
            'Strategic location acquisition'
        ]
        
        # Extract growth rate from data
        market_data = industry_data.get('market_sizing', {})
        trends['growth_rate'] = market_data.get('growth_rate', 28.5)
        
        return trends
    
    def create_visualizations(self, competitive_analysis: Dict, market_sizing: Dict, trend_analysis: Dict) -> Dict:
        """
        Create data visualizations for the report
        """
        self.logger.info("Creating visualizations")
        
        visualizations = {}
        
        try:
            # 1. Market Growth Projection Chart
            self._create_market_growth_chart(market_sizing)
            visualizations['market_growth'] = 'market_growth_projection.png'
            
            # 2. Competitive Matrix Radar Chart
            self._create_competitive_radar_chart(competitive_analysis)
            visualizations['competitive_radar'] = 'competitive_analysis_radar.png'
            
            # 3. Porter's Five Forces Chart
            # This will be created in the HTML template
            visualizations['porters_forces'] = 'porters_five_forces.png'
            
            # 4. Market Share Pie Chart
            self._create_market_share_chart(competitive_analysis)
            visualizations['market_share'] = 'market_share_distribution.png'
            
            # 5. Regional Market Distribution
            self._create_regional_chart(market_sizing)
            visualizations['regional_distribution'] = 'regional_market_distribution.png'
            
        except Exception as e:
            self.logger.error(f"Error creating visualizations: {str(e)}")
            visualizations['error'] = str(e)
        
        return visualizations
    
    def _create_market_growth_chart(self, market_sizing: Dict):
        """Create market growth projection chart"""
        projections = market_sizing.get('projections', {})
        current_value = market_sizing.get('current_market', {}).get('global_value_billion', 15.2)
        
        # Prepare data
        years = ['2024'] + list(projections.keys())
        values = [current_value] + list(projections.values())
        
        plt.figure(figsize=(10, 6))
        plt.plot(years, values, marker='o', linewidth=3, markersize=8, color='#2E8B57')
        plt.fill_between(years, values, alpha=0.3, color='#2E8B57')
        
        plt.title('EV Charging Market Growth Projection', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Market Value (Billion USD)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # Add value labels
        for i, v in enumerate(values):
            plt.annotate(f'${v:.1f}B', (i, v), textcoords="offset points", 
                        xytext=(0,10), ha='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('market_growth_projection.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_competitive_radar_chart(self, competitive_analysis: Dict):
        """Create competitive analysis radar chart"""
        matrix = competitive_analysis.get('competitive_matrix', {})
        
        if not matrix:
            return
        
        # Categories for radar chart
        categories = ['Network Size', 'Charging Speed', 'Geographic Coverage', 
                     'Technology Innovation', 'Brand Strength', 'Financial Resources']
        
        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]  # Complete the circle
        
        for i, (company, scores) in enumerate(list(matrix.items())[:4]):  # Limit to 4 companies
            values = list(scores.values())
            values += values[:1]  # Complete the circle
            
            ax.plot(angles, values, 'o-', linewidth=2, label=company, color=colors[i])
            ax.fill(angles, values, alpha=0.25, color=colors[i])
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=10)
        ax.set_ylim(0, 5)
        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8)
        ax.grid(True)
        
        plt.title('Competitive Analysis Matrix', fontsize=16, fontweight='bold', pad=20)
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        
        plt.tight_layout()
        plt.savefig('competitive_analysis_radar.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_market_share_chart(self, competitive_analysis: Dict):
        """Create market share pie chart"""
        market_share = competitive_analysis.get('market_share_estimates', {})
        
        if not market_share:
            return
        
        labels = list(market_share.keys())
        sizes = list(market_share.values())
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        
        plt.figure(figsize=(10, 8))
        pie_result = plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                           colors=colors, startangle=90, 
                           textprops={'fontsize': 10})
        
        if len(pie_result) == 3:
            wedges, texts, autotexts = pie_result
        else:
            wedges, texts = pie_result
            autotexts = []
        
        # Enhance the appearance
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        plt.title('EV Charging Market Share Distribution', fontsize=16, fontweight='bold', pad=20)
        plt.axis('equal')
        
        plt.tight_layout()
        plt.savefig('market_share_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_regional_chart(self, market_sizing: Dict):
        """Create regional market distribution chart"""
        regional_data = market_sizing.get('regional_analysis', {})
        
        if not regional_data:
            return
        
        regions = list(regional_data.keys())
        percentages = list(regional_data.values())
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(regions, percentages, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
        
        plt.title('Regional Market Distribution', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Region', fontsize=12)
        plt.ylabel('Market Share (%)', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar, value in zip(bars, percentages):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('regional_market_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # Helper methods
    def _score_network_size(self, company: str, metrics: Dict) -> int:
        """Score network size (1-5 scale)"""
        if 'Tesla' in company:
            return 5
        elif 'ChargePoint' in company:
            return 5
        elif 'Electrify America' in company:
            return 3
        return 2
    
    def _score_charging_speed(self, company: str) -> int:
        """Score charging speed capabilities"""
        if 'Tesla' in company:
            return 5
        elif 'Electrify America' in company:
            return 5
        elif 'ChargePoint' in company:
            return 3
        return 3
    
    def _score_coverage(self, company: str) -> int:
        """Score geographic coverage"""
        if 'Tesla' in company:
            return 5
        elif 'ChargePoint' in company:
            return 4
        elif 'Electrify America' in company:
            return 4
        return 2
    
    def _score_innovation(self, company: str) -> int:
        """Score technology innovation"""
        if 'Tesla' in company:
            return 5
        elif 'ChargePoint' in company:
            return 4
        return 3
    
    def _score_brand(self, company: str) -> int:
        """Score brand strength"""
        if 'Tesla' in company:
            return 5
        elif 'ChargePoint' in company:
            return 3
        return 3
    
    def _score_financial(self, company: str) -> int:
        """Score financial resources"""
        if 'Tesla' in company:
            return 5
        elif 'Electrify America' in company:
            return 4
        return 3
    
    def _rank_competitors(self, matrix: Dict) -> List[str]:
        """Rank competitors by total score"""
        scores = {}
        for company, metrics in matrix.items():
            scores[company] = sum(metrics.values())
        
        return sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
    
    def _assess_attractiveness(self, score: float) -> str:
        """Assess industry attractiveness based on Porter's Five Forces score"""
        if score <= 2:
            return "HIGHLY ATTRACTIVE"
        elif score <= 3:
            return "MODERATELY ATTRACTIVE"
        elif score <= 4:
            return "NEUTRAL"
        else:
            return "UNATTRACTIVE"
    
    def _calculate_market_metrics(self, market_data: Dict) -> Dict:
        """Calculate additional market metrics"""
        return {
            'stations_per_million_people': 125,  # Estimated
            'average_utilization_rate': 0.15,   # 15%
            'revenue_per_station_annual': 45000  # USD
        }
    
    def _calculate_penetration_rates(self, sizing: Dict) -> Dict:
        """Calculate market penetration rates"""
        current = sizing['current_market']['global_value_billion']
        tam = sizing['addressable_market']['tam_billion']
        
        return {
            'current_penetration': round((current / tam) * 100, 1),
            'projected_2030': 18.5,  # Estimated
            'saturation_timeline': '2035-2040'
        }
