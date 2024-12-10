# PART 1 - RESTRICTION CONFIGURATION
# Update the values below based on your needs

MAX_INPUT_TOKEN = 200 # Limit user input size
MAX_OUTPUT_TOKEN = 800 # Limit bot output size
NUMBER_OF_QUESTION = 20 # maximum number of question asked by users in a time window
PER_TIME_WINDOW = '10 minutes' # example: 'second' , '30 seconds', 'minute', '30 minutes', 'hour', '2 hours', 'day', '7 days'

# PART 2 - PERSONAL CONFIGURATION
# Update the values below with your personal details

# Default Assistant Prompt
ASSISTANT_PROMPT = "Always respond in a formal tone, be very welcoming, and provide helpful answers."

# Mandatory Fields
OWNER_FULL_NAME = "Anggoletomi Marlis Putra"
OWNER_NICK_NAME = "Anggo"

# Additional Fields (Optional: You can leave these blank if you feel they are not related to your personal details)
# If you choose to leave it blank, fill the blanks using "" or [] (following the original format)
# Note: The more information you provide, the better the assistant will understand and represent you
# IMPORTANT: Please follow the exact format:
# - Strings should be enclosed in quotes " "
# - Lists should be enclosed in square brackets [ ] with items separated by commas

OWNER_BIO = "Passionate about data, analytics, and intelligent automation"
OWNER_LINKEDIN = "https://www.linkedin.com/in/anggoletomi"
OWNER_WEBSITE = "https://anggoletomi.github.io/"

OWNER_SUMMARY = ["Business Intelligence Engineer with extensive experience in data analytics, automation, and business intelligence tools. "
                 "Specializing in delivering impactful data visualizations and optimizing end-to-end data pipelines. "
                 "Passionate about leveraging data to drive strategic decision-making and enhance business processes. "
                 "In the spare time, actively explore emerging AI technologies and applications, broadening expertise in tech-driven innovation. "
                 "unique background in sales and operations complements the technical skills, enabling to bridge the gap between data-driven insights and practical business strategies. "]

OWNER_EDUCATION = [
    "Bachelor's Degree in Industrial Engineering from Telkom University (August 2010 - June 2015). "
    "Focused on business process engineering, system modeling, design and analysis of information systems + database. "
    "Final Project Title: ILK Laundry Management Information System for transaction data and report using waterfall method. "
]

OWNER_CERTIFICATIONS = [
    "Data Science Certification from Rakamin Academy (August 2021 - November 2021). "
    "Focused on data cleansing, data analysis, data visualization, and building predictive models. "
    "Final Project Title: Credit Card Payment Default Prediction.",
    "Data Engineer Certification from DigitalSkola (January 2022 - April 2022). "
    "Focused on setting up, building, and managing data pipelines. "
    "Final Project Title: ETL Pipeline API Docker Airflow."
]

OWNER_EXPERIENCE = [
    "Business Intelligence Engineer at SCI Ecommerce (December 2019 - October 2024, Jakarta, Indonesia). "
    "1. Dashboard Development: Designed and delivered over five interactive dashboards and reports tailored for sales,marketing, supply chain, finance, and customer service teams. "
    "Providing actionable insights for stakeholders acrossmultiple countries in the SEA region. "
    "As part of a growing company, have demonstrated adaptability by developing dashboards using various BI visualization tools, including Looker Studio, Power BI, and FineBI. "
    "2. Data Pipeline and ETL Optimization: Automated and optimized end-to-end data pipelines using tools such as Python,SQL, and Power Automate. "
    "Streamlined the ETL process to efficiently process data from diverse sources, including over 100 e-commerce stores across four platforms (Tokopedia, Shopee, Lazada, and TikTok), eight WMS (Anchanto,Dilayani Tokopedia, Flash, Flux, Lazada BMS, Qianyi, Quick, and Qxpress), as well as email reports and Google Sheets. "
    "Each source featured unique reports and table schemas that required tailored processing. "
    "This automation replacedthe need for four dedicated personnel, reducing manual effort by approximately 330 hours per month and significantly minimizing human error. "
    "Achieved over 98% accuracy in data processing and improved report delivery time by 47%, enabling faster and more reliable decision-making. "
    "3. Advanced Analytics: Conducted in-depth data analysis using Python and SQL to identify key trends and provideactionable insights. "
    "Collaborated with the sales team to deliver recommendations based on critical performancemetrics. "
    "Created detailed inventory reports for the supply chain team, highlighting products nearing expiration,products aging in the warehouse, and products at risk of going out of stock that require prompt replenishment. "
    "Additionally, developed near real-time daily bottom-line reports, including net profit analysis, to identify products beingsold at a loss, pinpoint expense-related pain points, and support strategic decision-making. "
    "Analyzed in-platform adperformance metrics to evaluate spending efficiency, identify ROI, and recommend budget optimizations to maximizeoverall profitability. "
    "4. Cross-Functional Collaboration: Partnered with teams from sales, marketing, supply chain, finance, and customerservice teams to understand business needs and ensure data solutions aligned with strategic goals.",

    "Ecommerce Sales & Operation Lead at SCI Ecommerce (January 2019 - November 2019, Jakarta, Indonesia). "
    "Overseeing end-to-end e-commerce operations and driving business performance (top & bottom line). ",
    "Key Account Manager at Lazada (March 2016 - September 2018, Jakarta, Indonesia). "
    "Strategized to boost sales, managed client relationships, and evaluated sales performance indicators. "
]

OWNER_SPECIALIZATION = ["Data Collection","Data Cleansing","Data Modeling","Data Visualization","Data Analytics","Business Intelligence","Workflow Automation"]

OWNER_HARD_SKILLS = ["Python",
                     "Google Looker Studio","Tableau","Power BI","Fine BI",
                     "BigQuery","PostgreSQL","MySQL",
                     "Google Cloud Platform (GCP)","Virtual Machines (VMs)","SSH","Remote Server Management",
                     "Windows","Linux",
                     "Airflow","Microsoft Power Automate","Cronjobs",
                     "Excel","Google Sheets",
                     "REST API (basic knowledge)","Data Engineer (basic knowledge)","Machine Learning (basic knowledge)","Statistic (basic knowledge)"]

OWNER_SOFT_SKILLS = ["Effective Communication", "Critical Thinking", "Problem Solving", "Adaptability", 
                    "Logical Thinking", "Collaboration", "Time Management", "Attention to Detail", 
                    "Decision Making"]

OWNER_LANGUAGES = ["Indonesian", "English"]

# Add other information based on your needs
# You can create your own variable as long as it starts with 'OWNER_'
# Important: Fill the variables only with strings or lists.
# Example:
# OWNER_HOBBIES = ["Reading", "Traveling", "Gaming"]
# Add as many variables as you want to make the assistant more personalized!

OWNER_HOBBIES = ["Traveling","Swimming"]