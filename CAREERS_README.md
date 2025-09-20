# Careers Data Analysis

This directory contains career data and analysis tools for exploring diverse career opportunities.

## Files

- `careers.json` - Contains 25 diverse career entries with detailed information
- `careers_analyzer.py` - Main Python script for loading and querying career data
- `example_usage.py` - Example script demonstrating basic functionality
- `requirements.txt` - Python dependencies

## Career Data Structure

Each career entry contains:
- **id**: Unique identifier
- **title**: Job title
- **category**: Career category (Technology, Design, Marketing, etc.)
- **description**: Brief job description
- **required_skills**: List of required skills
- **experience_level**: Entry, Mid, or Senior level
- **salary_range**: Salary range in USD
- **education**: Educational requirements

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Example Script
```bash
python example_usage.py
```

### 3. Interactive Mode
```bash
python careers_analyzer.py --interactive
```

### 4. Command Line Usage
```bash
# Search by category
python careers_analyzer.py --category "Technology"

# Search by skill
python careers_analyzer.py --skill "Python"

# Search by experience level
python careers_analyzer.py --experience "Entry"

# Show high-salary careers
python careers_analyzer.py --high-salary 100000

# Export to CSV
python careers_analyzer.py --export careers_export.csv
```

## Available Career Categories

- **Technology** (10 careers): Software Engineer, Data Scientist, DevOps Engineer, etc.
- **Design** (2 careers): UX/UI Designer, Graphic Designer
- **Marketing** (4 careers): Digital Marketing Manager, Content Writer, etc.
- **Business** (5 careers): Product Manager, Business Analyst, etc.
- **Sales** (1 career): Sales Representative
- **Finance** (1 career): Financial Analyst
- **Human Resources** (1 career): Human Resources Manager

## Features

### Search Capabilities
- Search by category
- Search by required skills
- Search by experience level
- Filter by salary range
- Get detailed career information

### Data Analysis
- Category distribution
- Experience level breakdown
- Salary analysis
- Skill frequency analysis

### Export Options
- Export filtered results to CSV
- Export complete dataset

## Example Queries

```python
from careers_analyzer import CareersAnalyzer

# Initialize analyzer
analyzer = CareersAnalyzer()

# Get all technology careers
tech_careers = analyzer.get_tech_careers()

# Find careers requiring Python
python_careers = analyzer.search_by_skill("Python")

# Get high-salary careers
high_salary = analyzer.get_high_salary_careers(120000)

# Show career details
analyzer.display_career_details(1)
```

## Interactive Mode Features

The interactive mode provides a user-friendly menu with options to:
1. Search by category
2. Search by skill
3. Search by experience level
4. Show high-salary careers
5. Show tech careers
6. Show entry-level careers
7. Show career details by ID
8. Export to CSV
9. Show basic dataset information

## Career Data Sample

```json
{
  "id": 1,
  "title": "Software Engineer",
  "category": "Technology",
  "description": "Design, develop, and maintain software applications and systems using various programming languages and frameworks.",
  "required_skills": ["Programming", "Problem Solving", "Data Structures", "Algorithms", "Version Control"],
  "experience_level": "Entry to Senior",
  "salary_range": "$60,000 - $150,000",
  "education": "Bachelor's in Computer Science or related field"
}
```

## Requirements

- Python 3.7+
- pandas >= 2.0.0
- numpy >= 1.24.0

## Usage Tips

1. **Case-insensitive search**: All text searches are case-insensitive
2. **Partial matching**: Skills and categories support partial matching
3. **Multiple results**: Most queries return multiple results
4. **Detailed view**: Use career ID to get complete information
5. **Export data**: Use CSV export for further analysis in Excel or other tools
