import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import feedparser
import requests
from bs4 import BeautifulSoup

# ===== CONFIGURATION =====
EMAIL_ADDRESS = "giovannibwayo@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "xfgy cnrd suva raxv"    # Your Gmail app password 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
RECIPIENT_EMAIL = "giovannibwayo@gmail.com"

# ===== TEST FUNCTIONS =====
def test_email_connection():
    """Test if we can connect to Gmail SMTP server"""
    print("Testing email connection...")
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("✓ Email connection test PASSED")
        return True
    except Exception as e:
        print(f"✗ Email connection test FAILED: {e}")
        return False

def test_feed_parsing():
    """Test if we can parse RSS feeds"""
    print("Testing feed parsing...")
    
    test_feeds = [
        "https://www.esri.com/arcgis-blog/feed/",
        "https://arxiv.org/rss/cs.AI"
    ]
    
    successful_feeds = 0
    for feed_url in test_feeds:
        try:
            feed = feedparser.parse(feed_url)
            if feed.entries:
                print(f"✓ Feed '{feed_url}' has {len(feed.entries)} entries")
                successful_feeds += 1
            else:
                print(f"✗ Feed '{feed_url}' has no entries")
        except Exception as e:
            print(f"✗ Failed to parse feed '{feed_url}': {e}")
    
    return successful_feeds > 0

def test_content_extraction():
    """Test if we can extract content from a URL"""
    print("Testing content extraction...")
    
    test_urls = [
        "https://www.esri.com/arcgis-blog/overview/",
        "https://arxiv.org/list/cs.AI/recent"
    ]
    
    for url in test_urls:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"✓ Successfully accessed {url}")
                return True
            else:
                print(f"✗ Failed to access {url}: Status code {response.status_code}")
        except Exception as e:
            print(f"✗ Failed to access {url}: {e}")
    
    return False

def send_test_email():
    """Send a test email"""
    print("Sending test email...")
    
    try:
        msg = MIMEMultipart("alternative")
        msg['Subject'] = "Test: AI & GIS Daily Digest System"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        
        html_content = """
        <html>
        <body>
            <h2>Test Email from AI & GIS Daily Digest System</h2>
            <p>This is a test email sent at {}</p>
            <p>If you received this, the email system is working correctly!</p>
        </body>
        </html>
        """.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        msg.attach(MIMEText(html_content, "html"))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print("✓ Test email sent successfully!")
        return True
    except Exception as e:
        print(f"✗ Failed to send test email: {e}")
        return False

def get_sample_articles():
    """Get a few sample articles without sending email"""
    print("Fetching sample articles...")
    
    feeds = [
        "https://www.esri.com/arcgis-blog/feed/",
        "https://arxiv.org/rss/cs.AI"
    ]
    
    articles = []
    keywords = ["gis", "geospatial", "ai", "artificial intelligence", "machine learning"]
    
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:3]:  # Just get first 3 entries from each feed
                title = entry.title.lower()
                if any(keyword in title for keyword in keywords):
                    articles.append({
                        'title': entry.title,
                        'link': entry.link,
                        'source': feed_url,
                        'published': entry.get('published', 'Unknown date')
                    })
        except Exception as e:
            print(f"Error with feed {feed_url}: {e}")
    
    return articles

# ===== MAIN TEST =====
def run_tests():
    print("Running AI & GIS Daily Digest Tests")
    print("===================================")
    
    # Test 1: Email connection
    email_ok = test_email_connection()
    
    # Test 2: Feed parsing
    feeds_ok = test_feed_parsing()
    
    # Test 3: Content extraction
    content_ok = test_content_extraction()
    
    # Test 4: Send test email
    if email_ok:
        email_sent = send_test_email()
    else:
        email_sent = False
        print("Skipping email send test due to connection issues")
    
    # Test 5: Get sample articles
    articles = get_sample_articles()
    print(f"Found {len(articles)} relevant articles in sample")
    for i, article in enumerate(articles, 1):
        print(f"  {i}. {article['title']}")
    
    print("\nTest Results Summary")
    print("====================")
    print(f"Email Connection: {'PASS' if email_ok else 'FAIL'}")
    print(f"Feed Parsing: {'PASS' if feeds_ok else 'FAIL'}")
    print(f"Content Extraction: {'PASS' if content_ok else 'FAIL'}")
    print(f"Test Email: {'SENT' if email_sent else 'FAILED'}")
    print(f"Sample Articles: {len(articles)} found")
    
    if email_ok and feeds_ok:
        print("\n✓ Basic system functionality appears to be working!")
        print("You can now run the full script.")
    else:
        print("\n✗ Some tests failed. Please check your configuration.")
    
    return email_ok and feeds_ok

if __name__ == "__main__":
    run_tests()