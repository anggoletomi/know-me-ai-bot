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

OWNER_TITLE = "Business Intelligence Engineer, Data Analyst, AI Explorer"

OWNER_BIO = "Passionate about data, analytics, and intelligent automation"

OWNER_COUNTRY = "Indonesia"

OWNER_LINKEDIN = "https://www.linkedin.com/in/anggoletomi"

OWNER_WEBSITE = "https://anggoletomi.github.io/"

OWNER_GITHUB = "https://github.com/anggoletomi/"

OWNER_LIVEBOT = "https://know-me-ai-bot.onrender.com/"

OWNER_SUMMARY = ["I am a Business Intelligence Engineer with extensive experience in data analytics, automation, and business intelligence tools. "
                 "Specializing in delivering impactful data visualizations and optimizing end-to-end data pipelines, I am passionate about leveraging data to drive strategic decision-making and enhance business processes. "
                 "In my spare time, I actively explore emerging AI technologies and applications, broadening my expertise in tech-driven innovation. "
                 "My unique background in sales and operations complements my technical skills, enabling me to bridge the gap between data-driven insights and practical business strategies. "]

OWNER_SPECIALIZATION = ["Data Collection","Data Cleansing","Data Modeling","Data Visualization","Data Analytics",
                        "ETL","ELT","Data Engineer","Business Intelligence","Workflow Automation","Statistical Analysis",
                        "Basic Machine Learning"]

OWNER_EXPERIENCE = [
    "Business Intelligence Engineer at SCI Ecommerce (December 2019 - October 2024, Jakarta, Indonesia). "
    "1. Dashboard Development: Designed and delivered over five interactive dashboards and reports tailored for sales, marketing, supply chain, finance, and customer service teams, providing actionable insights for stakeholders across multiple countries in the SEA region. As part of a growing company, I have demonstrated adaptability by developing dashboards using various BI visualization tools, including Looker Studio, Power BI, and FineBI. "
    "2. Data Pipeline and ETL Optimization: Automated and optimized end-to-end data pipelines using tools such as Python, SQL, and Power Automate. Streamlined the ETL process to efficiently process data from diverse sources, including over 100 e-commerce stores across four platforms (Tokopedia, Shopee, Lazada, and TikTok), eight WMS (Anchanto, Dilayani Tokopedia, Flash, Flux, Lazada BMS, Qianyi, Quick, and Qxpress), as well as email reports and Google Sheets. Each source featured unique reports and table schemas that required tailored processing. This automation replaced the need for four dedicated personnel, reducing manual effort by approximately 330 hours per month and significantly minimizing human error. Achieved over 98% accuracy in data processing and improved report delivery time by 47%, enabling faster and more reliable decision-making. "
    "3. Advanced Analytics: Conducted in-depth data analysis using Python and SQL to identify key trends and provide actionable insights. Collaborated with the sales team to deliver recommendations based on critical performance metrics. Created detailed inventory reports for the supply chain team, highlighting products nearing expiration, products aging in the warehouse, and products at risk of going out of stock that require prompt replenishment. Additionally, developed near real-time daily bottom-line reports, including net profit analysis, to identify products being sold at a loss, pinpoint expense-related pain points, and support strategic decision-making. Analyzed in-platform ad performance metrics to evaluate spending efficiency, identify ROI, and recommend budget optimizations to maximize overall profitability. "
    "4. Cross-Functional Collaboration: Partnered with teams from sales, marketing, supply chain, finance, and customer service teams to understand business needs and ensure data solutions aligned with strategic goals. ",

    "Ecommerce Sales & Operation Lead at SCI Ecommerce (January 2019 - November 2019, Jakarta, Indonesia). "
    "Overseeing end-to-end e-commerce operations and driving business performance (top & bottom line). ",

    "Key Account Manager at Lazada (March 2016 - September 2018, Jakarta, Indonesia). "
    "1. Strategizes to boost sales through thorough business analysis, including sales projections and forecasting. "
    "2. Manages client relationships, negotiates deals, and regularly evaluates sales performance indicators. "
]

OWNER_EDUCATION = [
    "Bachelor's Degree in Industrial Engineering from Telkom University (August 2010 - June 2015, Bandung, Indonesia). "
]

OWNER_LANGUAGES = ["Indonesian (Native)", "English (Proficient)"]

OWNER_HARD_SKILLS = ["Programming Language : Python, R (Basic)",
                     "Data Visualization : Fine BI, Google Looker Studio, Power BI, Tableau",
                     "Databases & Data Storage : SQL (BigQuery, MySQL, PostgreSQL), NoSQL (MongoDB)",
                     "Cloud & Infrastructure : Docker, Google Cloud Platform (GCP), SSH & Remote Server Management, Virtual Machines (VMs)",
                     "Operating Systems & CLI : Terminal Scripting (Bash, Shell, CMD), Linux, Unix, Windows",
                     "Productivity & Office Tools : Google Sheets, Microsoft Excel",
                     "Data Engineering & Workflow Automation : Apache Airflow,APIs (REST, GraphQL),Cronjobs,Microsoft Power Automate, Version Control: Git (GitHub, GitLab, BitBucket)"
]

OWNER_SOFT_SKILLS = ["Effective Communication", "Critical Thinking", "Problem Solving", "Adaptability", 
                    "Logical Thinking", "Collaboration", "Time Management", "Attention to Detail", 
                    "Decision Making"]

OWNER_CERTIFICATIONS = [
    "Name: Google Data Analytics, Issuing Organization: Google, Issue Date: January 2025, Credential ID: JU5RPK0II6I6, Credential URL : https://www.coursera.org/account/accomplishments/professional-cert/certificate/JU5RPK0II6I6, Skills: Google Sheets, SQL, Tableau, R",
    "Name: Data Engineer, Issuing Organization: Digital Skola, Issue Date: May 2022, Credential ID: 22/SC/GRD/DE5/V/2022, Credential URL : https://drive.google.com/file/d/1--SkheDdgs0l56ns0vFpQANB30aILj-F/view?usp=sharing, Skills: Python, SQL, APIs, Linux, Unix, Virtual Machines",
    "Name: Data Scientist : Machine Learning, Issuing Organization: Rakamin Academy, Issue Date: November 2021, Credential ID: 507DS14112021, Credential URL : https://drive.google.com/file/d/127KgxV_72RNw0VWYhE8nA4CgEjtrU3a4/view?usp=sharing, Skills: Python, Machine Learning, SQL, Statistical Data Analysis",
]


# Add other information based on your needs
# You can create your own variable as long as it starts with 'OWNER_'
# Important: Fill the variables only with strings or lists.
# Example:
# OWNER_HOBBIES = ["Reading", "Traveling", "Gaming"]
# Add as many variables as you want to make the assistant more personalized!

OWNER_HOBBIES = ["Traveling","Swimming"]

OWNER_CAREER_GOALS = ["Interested in leading a data team within 3-5 years"]

OWNER_DESIRED_ROLE = ["Data Analytst", "Business Intelligence", "Data Engineer"]

OWNER_DESIRED_INDUSTRIES_OR_INDUSTRY_EXPOSURE = ["AI Native", "Cryptocurrency", "Financial", "Technology", "BI Service / Data Solution"]

OWNER_AVAILABILITY = "Available to start after a 1-month notice period"

OWNER_WORK_AUTHORIZATION = "Authorized to work in Indonesia, open to global remote opportunities"

OWNER_RELOCATION = "Open to relocating within Southeast Asia region"

OWNER_REMOTE_PREFERENCE = "Open to hybrid or fully remote roles"

OWNER_COMPENSATION_EXPECTATION = "Competitive with market standards, open to negotiation based on role and responsibilities"

OWNER_WORK_STYLE = "Analytical, detail-oriented, and collaborative, with a focus on delivering actionable insights"

OWNER_CORE_VALUES = ["Continuous Learning", "Integrity", "Customer-Centricity", "Innovation"]

OWNER_BENEFITS_IMPORTANCE = ["health coverage", "professional development budget", "flexible hours", "laptop budget support", "work remotely"]

OWNER_LEADERSHIP_STYLE = "Lead by example, encourage open communication, and foster a culture of continuous improvement."

OWNER_PROBLEM_SOLVING_APPROACH = "Understand context, break down problems, collaborate with stakeholders, iteratively refine solutions."

OWNER_COMMUNICATION_STYLE = "Convey technical details in relatable stories and visuals, adjusting language based on the audience."

OWNER_TEAM_CULTURE_FIT = "Enjoys diverse, collaborative, and continuous-learning teams that value innovation."

OWNER_CONTRACT_TYPE_PREFERENCE = "Permanent."

OWNER_FULLTIME_PARTTIME = 'Full Time.'

OWNER_EMPLOYER_VALUES = ["Innovation", "Professional Growth", "Ethical Conduct", "Diversity & Inclusion"]

OWNER_HR_QUESTIONS_AND_ANSWER = [
    "What are your strengths and weaknesses?|Strengths: I excel at overcoming new challenges and proactively solving problems with efficiency. I am detail-oriented, highly accurate, and well-organized, with strong documentation and communication skills. I take the initiative in breaking down complex problems into actionable steps and always strive for continuous learning. Weaknesses: I tend to take on too much responsibility myself because I want to ensure everything is done precisely. However, I am working on improving my delegation skills and learning to trust others to share responsibilities effectively. I'm not naturally confident in public speaking or presenting ideas to large groups. To address this, I've been practicing by participating in smaller meetings and preparing more thoroughly for presentations. I sometimes feel impatient when progress is slow, especially when I believe a task could be completed more efficiently. However, I've been working on improving my patience by understanding different working styles and focusing on collaboration to maintain a steady pace"
    "Why do you want to work here?|I want to work here because your company's focus aligns with my passion for leveraging data to drive insights and improve decision-making processes. I also value a collaborative and innovative work culture.",
    "What motivates you in your career?|I am motivated by solving complex problems, learning new skills, and creating impactful solutions that simplify decision-making for businesses.",
    "How do you handle stress or pressure at work?|I manage stress by breaking tasks into smaller steps, prioritizing effectively, and maintaining open communication with my team to ensure alignment.",
    "Can you describe a challenging situation you faced at work and how you handled it?|I struggled with isolation while working in a team spread across different time zones. To address this, I initiated regular updates and used collaboration tools to stay connected and ensure project alignment.",
    "What accomplishments are you most proud of?|I am most proud of my ability to innovate and create impactful solutions in environments without established systems. For example: I established Looker Studio dashboards to make data more accessible, even while data was still being manually inputted at that time, I created multiple automation tools that streamlined manual workflows, saving time and improving accuracy. I also introduced data-driven decision-making practices that shifted the company culture towards relying on insights rather than intuition. Seeing my ideas applied and helping others succeed has been incredibly rewarding",
    "Why are you leaving (or why did you leave) your current/previous job?|I left because I felt limited in opportunities for growth and lacked alignment with the work environment. I am seeking a fully remote role to focus on productivity and collaboration.",
    "What have you learned from your past mistakes at work?|I learned the importance of seeking clarity and aligning expectations early to avoid miscommunication and inefficiencies.",
    "Can you give an example of a time you demonstrated leadership?|I led a project to design and implement an automated reporting system, coordinating across teams and ensuring its timely delivery.",
    "How do you handle conflict in a team setting?|I address conflict by listening to all perspectives, identifying the root cause, and finding a solution that benefits the team as a whole.",
    "Describe a time when you worked with a difficult colleague and how you managed it.|I worked with a colleague who was resistant to adopting a new tool. I addressed this by demonstrating the tool's benefits and providing hands-on support to ease the transition.",
    "How do you ensure effective communication in a team?|I ensure effective communication by setting clear expectations, using collaboration tools, and scheduling regular check-ins to stay aligned.",
    "What role do you usually take in a team?|I usually take on the role of a data strategist or problem-solver, ensuring tasks are completed efficiently and with high quality.",
    "What do you know about our company and its culture?|I know your company values innovation, collaboration, and data-driven decision-making, which aligns with my career goals and values.",
    "How do your skills and experience align with the requirements of this role?|My skills in BI tools, data visualization, and automation align closely with this role, along with my ability to adapt and learn quickly in new environments.",
    "Where do you see yourself in five years?|I see myself as a senior data analyst or BI consultant, contributing to impactful projects and mentoring others in the field.",
    "What are your salary expectations?|My expectation is competitive with market standards for this role and level of expertise, and I am open to negotiation.",
    "Are you open to travel if the job requires it?|I am open to occasional travel if necessary."
]
