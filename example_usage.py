#!/usr/bin/env python3
"""
Example usage of the CareersAnalyzer script.
This demonstrates basic functionality for loading and querying career data.
"""

from careers_analyzer import CareersAnalyzer

def main():
    print("🚀 Careers Data Analysis Example")
    print("=" * 50)
    
    # Initialize the analyzer
    analyzer = CareersAnalyzer("careers.json")
    
    if analyzer.df.empty:
        print("❌ Could not load career data. Please check if careers.json exists.")
        return
    
    # Show basic information
    analyzer.get_basic_info()
    
    # Example 1: Search for technology careers
    print("\n" + "="*60)
    print("🔍 EXAMPLE 1: Technology Careers")
    print("="*60)
    tech_careers = analyzer.get_tech_careers()
    analyzer.display_results(tech_careers, "Technology Careers")
    
    # Example 2: Search for careers requiring Python
    print("\n" + "="*60)
    print("🔍 EXAMPLE 2: Careers Requiring Python")
    print("="*60)
    python_careers = analyzer.search_by_skill("Python")
    analyzer.display_results(python_careers, "Careers requiring Python")
    
    # Example 3: High-salary careers
    print("\n" + "="*60)
    print("🔍 EXAMPLE 3: High-Salary Careers ($100,000+)")
    print("="*60)
    high_salary = analyzer.get_high_salary_careers(100000)
    analyzer.display_results(high_salary, "High-salary careers")
    
    # Example 4: Entry-level careers
    print("\n" + "="*60)
    print("🔍 EXAMPLE 4: Entry-Level Careers")
    print("="*60)
    entry_level = analyzer.get_entry_level_careers()
    analyzer.display_results(entry_level, "Entry-level careers")
    
    # Example 5: Show details for a specific career
    print("\n" + "="*60)
    print("🔍 EXAMPLE 5: Career Details (ID: 1)")
    print("="*60)
    analyzer.display_career_details(1)
    
    # Example 6: Export to CSV
    print("\n" + "="*60)
    print("🔍 EXAMPLE 6: Export to CSV")
    print("="*60)
    analyzer.export_to_csv("careers_export.csv")
    
    print("\n✅ Example completed! You can now run the interactive mode:")
    print("   python careers_analyzer.py --interactive")

if __name__ == "__main__":
    main()
