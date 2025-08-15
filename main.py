"""
EV Charging Industry Analysis - Main Application
Comprehensive consulting-style report generator for EV charging industry trends and competitive landscape
"""

import os
import json
import logging
from datetime import datetime
from data_collector import DataCollector
from analysis_engine import AnalysisEngine
from report_generator import ReportGenerator
from utils import setup_logging, create_directories

def main():
    """Main function to orchestrate the EV charging industry analysis"""
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting EV Charging Industry Analysis")
    print("🚗⚡ EV Charging Industry Analysis - Consulting Report Generator")
    print("=" * 60)
    
    try:
        # Create necessary directories
        create_directories()
        
        # Initialize components
        print("📊 Initializing data collection...")
        data_collector = DataCollector()
        
        print("🔍 Initializing analysis engine...")
        analysis_engine = AnalysisEngine()
        
        print("📋 Initializing report generator...")
        report_generator = ReportGenerator()
        
        # Step 1: Data Collection
        print("\n🌐 Collecting industry data...")
        industry_data = data_collector.collect_all_data()
        
        if not industry_data:
            logger.error("Failed to collect sufficient data")
            print("❌ Error: Unable to collect sufficient data for analysis")
            return
        
        print(f"✅ Successfully collected data from {len(industry_data)} sources")
        
        # Step 2: Competitive Analysis
        print("\n🏢 Performing competitive analysis...")
        competitive_analysis = analysis_engine.analyze_competitors(industry_data)
        
        # Step 3: Porter's Five Forces Analysis
        print("\n⚔️ Conducting Porter's Five Forces analysis...")
        porters_analysis = analysis_engine.porters_five_forces(industry_data)
        
        # Step 4: SWOT Analysis
        print("\n📈 Generating SWOT analysis...")
        swot_analysis = analysis_engine.swot_analysis(industry_data)
        
        # Step 5: Market Sizing
        print("\n💰 Calculating market sizing...")
        market_sizing = analysis_engine.market_sizing(industry_data)
        
        # Step 6: Trend Analysis
        print("\n📊 Analyzing industry trends...")
        trend_analysis = analysis_engine.trend_analysis(industry_data)
        
        # Step 7: Generate Visualizations
        print("\n📈 Creating data visualizations...")
        visualizations = analysis_engine.create_visualizations(
            competitive_analysis, market_sizing, trend_analysis
        )
        
        # Step 8: Compile Final Report
        print("\n📄 Generating professional report...")
        report_data = {
            'metadata': {
                'generated_date': datetime.now().strftime('%B %d, %Y'),
                'generated_time': datetime.now().strftime('%H:%M UTC'),
                'report_version': '1.0'
            },
            'industry_data': industry_data,
            'competitive_analysis': competitive_analysis,
            'porters_analysis': porters_analysis,
            'swot_analysis': swot_analysis,
            'market_sizing': market_sizing,
            'trend_analysis': trend_analysis,
            'visualizations': visualizations
        }
        
        # Generate reports
        html_report = report_generator.generate_html_report(report_data)
        markdown_report = report_generator.generate_markdown_report(report_data)
        
        # Save reports
        html_filename = 'ev_charging_analysis_report.html'
        md_filename = 'ev_charging_analysis_report.md'
        
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_report)
        
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_report)
        
        # Save raw data for reference
        with open('analysis_data.json', 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, default=str)
        
        print("\n✅ Analysis complete! Reports generated:")
        print("   📄 ev_charging_analysis_report.html")
        print("   📝 ev_charging_analysis_report.md")
        print("   📊 analysis_data.json")
        print("   📈 Visualization charts saved as PNG files")
        
        print("\n🎯 Key Findings Summary:")
        
        # Display executive summary
        if market_sizing and 'market_value_billion' in market_sizing:
            print(f"   💰 Global EV Charging Market: ${market_sizing['market_value_billion']:.1f}B")
        
        if trend_analysis and 'growth_rate' in trend_analysis:
            print(f"   📈 Annual Growth Rate: {trend_analysis['growth_rate']:.1f}%")
        
        if competitive_analysis and 'top_players' in competitive_analysis:
            print(f"   🏢 Top Players: {', '.join(competitive_analysis['top_players'][:3])}")
        
        print("\n🚀 Report ready for stakeholder presentation!")
        
        logger.info("EV Charging Industry Analysis completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        print(f"❌ Error: {str(e)}")
        print("Please check the logs for detailed error information.")

if __name__ == "__main__":
    main()
