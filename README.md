# Simple README for News Scrapers

```markdown
# News Scrapers

Automated news digest systems for AI, GIS, and Data Science trends.

##  Overview

This repository contains two Python scripts that automatically curate and send email digests:

1. **Daily AI & GIS Digest** - Sends daily articles at 8:00 AM
2. **Weekly Trends Digest** - Sends industry trends every Monday at 8:00 AM

##  Quick Setup

### Prerequisites
- Python 3.7+
- Gmail account with App Password

### Installation
1. Clone the repository:
```bash
git clone https://github.com/GIOVESS/news-scrapers.git
cd news-scrapers
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your email settings in both scripts:
   - Edit `ai_gis_digest.py` and `weekly_trends_digest.py`
   - Set your Gmail address and App Password:
   ```python
   EMAIL_ADDRESS = "your.email@gmail.com"
   EMAIL_PASSWORD = "your-app-password"
   ```

### Gmail App Password Setup
1. Enable 2-Step Verification on your Google Account
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a new app password for "Mail"
4. Use this 16-character password in the scripts

##  Scripts

### 1. Daily AI & GIS Digest (`ai_gis_digest.py`)
- **Schedule**: Daily at 8:00 AM
- **Content**: Curated AI and GIS articles from multiple sources
- **Features**: Relevance scoring, top 10 articles, HTML formatting

### 2. Weekly Trends Digest (`weekly_trends_digest.py`) 
- **Schedule**: Every Monday at 8:00 AM
- **Content**: Industry trends and developments in GIS, AI, and Data Science
- **Features**: Trend detection, impact scoring, professional formatting

##  Windows Task Automation

### Method 1: Using Task Scheduler (Recommended)

#### For Daily Digest:
1. Open Task Scheduler
2. Create Basic Task:
   - Name: `Daily AI GIS Digest`
   - Trigger: Daily at 8:00 AM
   - Action: Start a program
   - Program: `python`
   - Arguments: `E:\PROJECT\news-scrapers\ai_gis_digest.py`
   - Start in: `E:\PROJECT\news-scrapers`

#### For Weekly Digest:
1. Open Task Scheduler  
2. Create Basic Task:
   - Name: `Weekly GIS AI Trends`
   - Trigger: Weekly on Mondays at 8:00 AM
   - Action: Start a program
   - Program: `python`
   - Arguments: `E:\PROJECT\news-scrapers\weekly_trends_digest.py`
   - Start in: `E:\PROJECT\news-scrapers`

### Method 2: Batch Files (Alternative)

Create `start_daily.bat`:
```batch
@echo off
cd /d "E:\PROJECT\news-scrapers"
python ai_gis_digest.py
```

Create `start_weekly.bat`:
```batch  
@echo off
cd /d "E:\PROJECT\news-scrapers"
python weekly_trends_digest.py
```

Schedule these batch files using Task Scheduler.

##  Testing

Test each script manually first:

```bash
# Test daily digest
python ai_gis_digest.py

# Test weekly trends  
python weekly_trends_digest.py
```

Check your email to verify the digests are working correctly.

##  Project Structure

```
news-scrapers/
├── ai_gis_digest.py          # Daily article digest
├── weekly_trends_digest.py   # Weekly trends digest  
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── .gitignore              # Git ignore file
```

##  Troubleshooting

### Common Issues:
1. **SMTP Authentication Error**: Verify your App Password is correct
2. **No Articles Found**: Check internet connection and source availability
3. **Script Stops**: Ensure Python is in system PATH

### Logs:
- Check console output for errors
- Scripts print status messages with timestamps

##  License

MIT License - feel free to use and modify for your needs.

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Maintainer**: Giovanni Bwayo  
**Portfolio**: giovannibwayo.site
```

## Git Push Commands

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Add news scraper scripts and documentation"

# Add remote origin
git remote add origin https://github.com/GIOVESS/news-scrapers.git

# Push to main branch
git branch -M main
git push -u origin main
```


