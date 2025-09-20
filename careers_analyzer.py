#!/usr/bin/env python3
"""
Careers Data Analyzer
A Python script to load and query career data from careers.json using pandas.
"""

import pandas as pd
import json
from typing import List, Dict, Any
import argparse

class CareersAnalyzer:
    def __init__(self, json_file: str = "careers.json"):
        """Initialize the analyzer with career data from JSON file."""
        self.json_file = json_file
        self.df = self.load_data()
    
    def load_data(self) -> pd.DataFrame:
        """Load career data from JSON file into a pandas DataFrame."""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Convert to DataFrame
            df = pd.DataFrame(data)
            
            # Convert skills list to string for better display
            df['required_skills'] = df['required_skills'].apply(lambda x: ', '.join(x))
            
            print(f"✅ Successfully loaded {len(df)} career entries from {self.json_file}")
            return df
            
        except FileNotFoundError:
            print(f"❌ Error: {self.json_file} not found!")
            return pd.DataFrame()
        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON format in {self.json_file}")
            return pd.DataFrame()
    
    def get_basic_info(self) -> None:
        """Display basic information about the dataset."""
        if self.df.empty:
            return
        
        print("\n📊 DATASET OVERVIEW")
        print("=" * 50)
        print(f"Total careers: {len(self.df)}")
        print(f"Categories: {self.df['category'].nunique()}")
        print(f"Experience levels: {self.df['experience_level'].nunique()}")
        
        print("\n📈 CATEGORY DISTRIBUTION")
        print("-" * 30)
        category_counts = self.df['category'].value_counts()
        for category, count in category_counts.items():
            print(f"{category}: {count} careers")
        
        print("\n🎯 EXPERIENCE LEVEL DISTRIBUTION")
        print("-" * 35)
        exp_counts = self.df['experience_level'].value_counts()
        for level, count in exp_counts.items():
            print(f"{level}: {count} careers")
    
    def search_by_category(self, category: str) -> pd.DataFrame:
        """Search careers by category."""
        if self.df.empty:
            return pd.DataFrame()
        
        result = self.df[self.df['category'].str.contains(category, case=False, na=False)]
        return result
    
    def search_by_skill(self, skill: str) -> pd.DataFrame:
        """Search careers that require a specific skill."""
        if self.df.empty:
            return pd.DataFrame()
        
        result = self.df[self.df['required_skills'].str.contains(skill, case=False, na=False)]
        return result
    
    def search_by_experience_level(self, level: str) -> pd.DataFrame:
        """Search careers by experience level."""
        if self.df.empty:
            return pd.DataFrame()
        
        result = self.df[self.df['experience_level'].str.contains(level, case=False, na=False)]
        return result
    
    def get_high_salary_careers(self, min_salary: int = 100000) -> pd.DataFrame:
        """Get careers with salary ranges above a certain threshold."""
        if self.df.empty:
            return pd.DataFrame()
        
        # Extract numeric values from salary range (simplified approach)
        def extract_max_salary(salary_str):
            try:
                # Extract the higher number from salary range like "$60,000 - $150,000"
                import re
                numbers = re.findall(r'\$?([0-9,]+)', salary_str)
                if len(numbers) >= 2:
                    return int(numbers[1].replace(',', ''))
                return 0
            except:
                return 0
        
        self.df['max_salary'] = self.df['salary_range'].apply(extract_max_salary)
        result = self.df[self.df['max_salary'] >= min_salary]
        return result[['title', 'category', 'salary_range', 'required_skills']]
    
    def get_tech_careers(self) -> pd.DataFrame:
        """Get all technology-related careers."""
        return self.search_by_category("Technology")
    
    def get_entry_level_careers(self) -> pd.DataFrame:
        """Get careers suitable for entry-level candidates."""
        return self.search_by_experience_level("Entry")
    
    def display_career_details(self, career_id: int) -> None:
        """Display detailed information about a specific career."""
        if self.df.empty:
            return
        
        career = self.df[self.df['id'] == career_id]
        if career.empty:
            print(f"❌ Career with ID {career_id} not found!")
            return
        
        career = career.iloc[0]
        print(f"\n🎯 CAREER DETAILS: {career['title']}")
        print("=" * 60)
        print(f"ID: {career['id']}")
        print(f"Category: {career['category']}")
        print(f"Description: {career['description']}")
        print(f"Experience Level: {career['experience_level']}")
        print(f"Salary Range: {career['salary_range']}")
        print(f"Education: {career['education']}")
        print(f"Required Skills: {career['required_skills']}")
    
    def export_to_csv(self, filename: str = "careers_export.csv") -> None:
        """Export the career data to CSV file."""
        if self.df.empty:
            return
        
        self.df.to_csv(filename, index=False)
        print(f"✅ Data exported to {filename}")
    
    def interactive_search(self) -> None:
        """Interactive search interface."""
        while True:
            print("\n🔍 INTERACTIVE CAREER SEARCH")
            print("=" * 40)
            print("1. Search by category")
            print("2. Search by skill")
            print("3. Search by experience level")
            print("4. Show high-salary careers")
            print("5. Show tech careers")
            print("6. Show entry-level careers")
            print("7. Show career details by ID")
            print("8. Export to CSV")
            print("9. Show basic info")
            print("0. Exit")
            
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == "0":
                print("👋 Goodbye!")
                break
            elif choice == "1":
                category = input("Enter category to search: ").strip()
                results = self.search_by_category(category)
                self.display_results(results, f"Careers in '{category}'")
            elif choice == "2":
                skill = input("Enter skill to search: ").strip()
                results = self.search_by_skill(skill)
                self.display_results(results, f"Careers requiring '{skill}'")
            elif choice == "3":
                level = input("Enter experience level: ").strip()
                results = self.search_by_experience_level(level)
                self.display_results(results, f"Careers for '{level}' level")
            elif choice == "4":
                min_sal = input("Enter minimum salary (default 100000): ").strip()
                min_sal = int(min_sal) if min_sal.isdigit() else 100000
                results = self.get_high_salary_careers(min_sal)
                self.display_results(results, f"High-salary careers (${min_sal}+)")
            elif choice == "5":
                results = self.get_tech_careers()
                self.display_results(results, "Technology Careers")
            elif choice == "6":
                results = self.get_entry_level_careers()
                self.display_results(results, "Entry-Level Careers")
            elif choice == "7":
                career_id = input("Enter career ID: ").strip()
                if career_id.isdigit():
                    self.display_career_details(int(career_id))
                else:
                    print("❌ Please enter a valid career ID!")
            elif choice == "8":
                filename = input("Enter CSV filename (default: careers_export.csv): ").strip()
                filename = filename if filename else "careers_export.csv"
                self.export_to_csv(filename)
            elif choice == "9":
                self.get_basic_info()
            else:
                print("❌ Invalid choice! Please try again.")
    
    def display_results(self, results: pd.DataFrame, title: str) -> None:
        """Display search results in a formatted way."""
        if results.empty:
            print(f"\n❌ No careers found for: {title}")
            return
        
        print(f"\n📋 {title.upper()}")
        print("=" * len(title) + "=" * 10)
        print(f"Found {len(results)} career(s):\n")
        
        for _, career in results.iterrows():
            print(f"🔹 {career['title']} (ID: {career['id']})")
            print(f"   Category: {career['category']}")
            print(f"   Experience: {career['experience_level']}")
            print(f"   Salary: {career['salary_range']}")
            print(f"   Skills: {career['required_skills'][:100]}{'...' if len(career['required_skills']) > 100 else ''}")
            print()

def main():
    """Main function to run the careers analyzer."""
    parser = argparse.ArgumentParser(description="Analyze career data from JSON file")
    parser.add_argument("--file", "-f", default="careers.json", help="Path to careers JSON file")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")
    parser.add_argument("--category", "-c", help="Search by category")
    parser.add_argument("--skill", "-s", help="Search by skill")
    parser.add_argument("--experience", "-e", help="Search by experience level")
    parser.add_argument("--high-salary", type=int, help="Show careers with salary above this amount")
    parser.add_argument("--export", help="Export to CSV file")
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = CareersAnalyzer(args.file)
    
    if analyzer.df.empty:
        return
    
    # Show basic info
    analyzer.get_basic_info()
    
    # Handle command line arguments
    if args.interactive:
        analyzer.interactive_search()
    else:
        if args.category:
            results = analyzer.search_by_category(args.category)
            analyzer.display_results(results, f"Careers in '{args.category}'")
        
        if args.skill:
            results = analyzer.search_by_skill(args.skill)
            analyzer.display_results(results, f"Careers requiring '{args.skill}'")
        
        if args.experience:
            results = analyzer.search_by_experience_level(args.experience)
            analyzer.display_results(results, f"Careers for '{args.experience}' level")
        
        if args.high_salary:
            results = analyzer.get_high_salary_careers(args.high_salary)
            analyzer.display_results(results, f"High-salary careers (${args.high_salary}+)")
        
        if args.export:
            analyzer.export_to_csv(args.export)

if __name__ == "__main__":
    main()
