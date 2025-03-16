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

OWNER_TITLE = "Business Intelligence Analyst, Data Analyst"

OWNER_BIO = "Passionate about data, analytics, and intelligent automation"

OWNER_COUNTRY = "Indonesia"

OWNER_LINKEDIN = "https://www.linkedin.com/in/anggoletomi"

OWNER_WEBSITE = "https://anggoletomi.github.io/"

OWNER_GITHUB = "https://github.com/anggoletomi/"

OWNER_LIVEBOT = "https://know-me-ai-bot.onrender.com/"

OWNER_SUMMARY = ["Business Intelligence and Data Analyst with over 5 years of experience turning numbers into clear insights. "
                 "I enjoy building dashboards that help teams solve real business problems and make decisions faster. "
                 "I've worked on automating reports and data pipelines to save time and cut costs. "
                 "My goal is to find the story behind the data and share it in a way everyone can understand. "
                 "I'm also eager to learn new analytics tools and AI trends to keep delivering fresh ideas. "
                 "If you need someone who loves digging into data and making an impact, I'd be excited to help. "]

OWNER_SPECIALIZATION = ["Data Visualization & BI Tools","Analytics & Reporting","SQL & Data Modeling",
                        "Statistical Analysis","ETL/ELT & Workflow Automation","Data Quality & Governance",
                        "Basic Machine Learning","Descriptive/Exploratory Data Analysis"]

OWNER_HARD_SKILLS = ["Programming & Scripting: Python, R",
                     "Data Visualization & BI Tools: FineBI, Google Looker Studio, Metabase, Power BI, Tableau",
                     "Databases & Data Storage : Data Lake (S3, HDFS), Data Warehouse (BigQuery, Redshift, Snowflake), NoSQL (MongoDB), SQL (MySQL, PostgreSQL)",
                     "Cloud & Infrastructure: Amazon Web Services (AWS), Docker, Google Cloud Platform (GCP), SSH & Remote Server Management, Virtual Machines (VMs)",
                     "Operating Systems & CLI: Terminal Scripting (Bash, Shell, CMD), Linux, Windows",
                     "Productivity & Office Tools: Google Sheets, Microsoft Excel",
                     "Data Engineering & Workflow Automation: Apache Airflow, Apache Hadoop, Apache Hive, APIs (REST, GraphQL), CI/CD Tools: GitHub Actions, Cronjobs, dbt, Microsoft Power Automate, Version Control: Git (GitHub, GitLab, BitBucket)"
                    ]

OWNER_EXPERIENCE = [
    "Senior Data Analyst at SALT (February 2025 - Current, Jakarta, Indonesia): "
    "1. Created dashboards for our client (Telkomsel) using internal BI tools, ensuring accurate queries and efficient loading times for financial, subscriber, sales, traffic, and customer care data. "
    "2. Developed predictive models for payment fault and churn, providing proactive insights for retention and risk management. "
    "3. Ensured data accuracy, integrity, consistency, and completeness by developing an alert system to detect and flag any data anomalies. "
    "4. Built KPI-tracking dashboards and regularly presented performance reports. "
    "5. Led churn analysis and customer segmentation to drive user retention and targeted marketing strategies, enhancing ARPU (Average Revenue Per User) through data-driven upsell initiatives and tailored bundle offerings. "
    "6. Conducted marketing campaign evaluations via A/B testing for each new service package, followed by statistical analyses to measure the significance of performance differences. ",
    
    "Business Intelligence Analyst at SCI Ecommerce (December 2019 - October 2024, Jakarta, Indonesia): "
    "1. Created and maintained 5+ interactive BI dashboards (sales, marketing, supply chain, finance) for over 100 stakeholders in SEA, helping teams make decisions faster and cutting reporting time by 40%. "
    "2. Integrated data from various sources with 98% accuracy, saving 330 hours/month by reducing manual work. "
    "3. Led analytics projects to find cost savings and optimize inventory, lowering holding costs by 10%. "
    "4. Worked with different teams to set KPIs and design dashboards, ensuring they matched company goals. "
    "5. Collaborated with cross-functional teams to align data solutions with strategic and operational goals. "
    "Key Projects: "
    "Market Basket Analysis: Used the Apriori algorithm to identify frequently purchased product bundles, leading to a 12% increase in average order value. Reduced unsold aging stock by 15% through targeted cross-selling and bundle promotions. "
    "Sales Trend Analysis: Ran time-series studies that pinpointed best/worst sales hours, boosting flash sale conversion by 25% when applied to peak traffic times. "
    "Inventory Reports: Built reports that track stock levels, aging products, and near-expired items, plus suggestions for reorder amounts to avoid running out of stock. "
    "Brand Evaluation: Create a brand evaluation template to negotiate strategic fee models that improve net profit margins. "
    "Monthly Business Review: Helped the sales team create monthly review report for brand clients. Streamlined the review process, resulting in fewer data discrepancies and faster approvals for next month’s budget. "
    "Campaign Activity & Ad Performance: Evaluated ROI of campaigns and ads to identify best practices for future events. "
    "Packaging Efficiency: Found the most suitable packaging based on product type and sales volume, reducing wasted space and costs. "

    "Ecommerce Sales & Operation Lead at SCI Ecommerce (January 2019 - November 2019, Jakarta, Indonesia): "
    "1. Utilized sales data and performance metrics to forecast demand and optimize inventory levels, reducing stockouts and operational costs. "
    "2. Maintained weekly analytics dashboards to track KPIs, delivering actionable insights to leadership for improved promotional strategies and revenue growth. ",

    "Key Account Manager at Lazada (March 2016 - September 2018, Jakarta, Indonesia): "
    "1. Conducted data-driven sales forecasting and trend analysis to set realistic targets, optimize promotional efforts, and improve account performance. "
    "2. Regularly reviewed KPIs with clients, translating insights into strategic account expansions and data-informed negotiations. "
]

OWNER_CERTIFICATIONS = [
    "Name: Google Data Analytics, Issuing Organization: Google, Issue Date: January 2025, Credential ID: JU5RPK0II6I6, Credential URL : https://www.coursera.org/account/accomplishments/professional-cert/certificate/JU5RPK0II6I6, Skills: Google Sheets, SQL, Tableau, R",
    "Name: Data Engineer, Issuing Organization: Digital Skola, Issue Date: May 2022, Credential ID: 22/SC/GRD/DE5/V/2022, Credential URL : https://drive.google.com/file/d/1--SkheDdgs0l56ns0vFpQANB30aILj-F/view?usp=sharing, Skills: Python, SQL, APIs, Linux, Unix, Virtual Machines",
    "Name: Data Scientist : Machine Learning, Issuing Organization: Rakamin Academy, Issue Date: November 2021, Credential ID: 507DS14112021, Credential URL : https://drive.google.com/file/d/127KgxV_72RNw0VWYhE8nA4CgEjtrU3a4/view?usp=sharing, Skills: Python, Machine Learning, SQL, Statistical Data Analysis",
]

OWNER_LANGUAGES = ["Indonesian (Native)", "English (Proficient)"]

OWNER_EDUCATION = [
    "Bachelor's Degree in Industrial Engineering from Telkom University (August 2010 - June 2015, Bandung, Indonesia). "
]

OWNER_PROJECT_PORTFOLIO = ["For a complete list of my projects, please visit my Github Pages : https://anggoletomi.github.io"
                           "1. Generalized Recommendation System: Focused on building a comprehensive recommendation system pipeline. Covering data preprocessing, model training, and performance evaluation. It can be adapted for recommending books, movies, products, and more. Git : https://github.com/anggoletomi/generalized-recommendation-system"
                           "2. Leveraging Market Basket Analysis: Unearthing Hidden Gems in Sales Data. Kaggle : https://www.kaggle.com/code/anggoletomi/unearthing-hidden-gems-in-your-sales-data"
                           ]

# Add other information based on your needs
# You can create your own variable as long as it starts with 'OWNER_'
# Important: Fill the variables only with strings or lists.
# Example:
# OWNER_HOBBIES = ["Traveling","Swimming","Reading"]
# Add as many variables as you want to make the assistant more personalized!

OWNER_WORK_ETHIC = ["I respect time and commitments.",
                    "I deliver high-quality work.",
                    "I am someone you can count on, and I make myself available when needed.",
                    "I am honest about mistakes and take responsibility for correcting them without shifting blame.", 
                    "I take ownership of tasks and outcomes, ensuring I follow through on my commitments.", 
                    "I put in the effort to exceed expectations.",
                    "I learn new skills to enhance my performance.",
                    "I adjust to changes in project requirements and quickly learn new tools to ensure success.",
                    "I pay close attention to detail by double-checking data for errors and revising reports to ensure accuracy before submission.",
                    "I figure out how to use new software tools on my own by reading documentation and watching tutorials, rather than waiting for formal training.",
                    "I continue troubleshooting complex technical issues until I find a solution, demonstrating determination and commitment to excellence.",
                    "I take courses to enhance my skills.",
                    "I prioritize tasks by importance and urgency, completing critical reports first before responding to routine emails.",
                    "I acknowledge when I don't know the answer and commit to finding out and following up promptly.",
                    "I go above and beyond minimum requirements.",
                    "I identify the root cause of recurring issue and implement permanent fixes rather than relying on temporary workarounds.",
                    "I take full accountability for mistakes and immediately work to correct them, ensuring they don't happen again.",
                    "I maintain a mindset of constant improvement, always seeking new and better ways to do things rather than settling for the status quo.",
                    "I manage my responsibilities independently, stay motivated, and uphold high performance standards even without direct supervision."]

OWNER_HOBBIES = ["Traveling","Swimming","Reading"]

OWNER_CAREER_GOALS = ["Interested in leading a data team within 3-5 years"]

OWNER_DESIRED_ROLE = ["Business Intelligence Analyst", "Data Analytst"]

OWNER_DESIRED_INDUSTRIES_OR_INDUSTRY_EXPOSURE = ["AI Native", "Cryptocurrency", "Financial", "Technology", "BI Service / Data Solution"]

OWNER_AVAILABILITY = "Available to start immediately as soon as possible"

OWNER_WORK_AUTHORIZATION = "Authorized to work in Indonesia, open to global remote opportunities"

OWNER_RELOCATION = "Open to relocating within Southeast Asia region"

OWNER_REMOTE_PREFERENCE = "Open to hybrid or fully remote roles"

OWNER_COMPENSATION_EXPECTATION = "Competitive with market standards, open to negotiation based on role and responsibilities"

OWNER_CONTRACT_TYPE_PREFERENCE = "Permanent."

OWNER_FULLTIME_PARTTIME = 'Full Time.'

OWNER_BENEFITS_IMPORTANCE = ["health coverage", "professional development budget", "flexible hours", "laptop budget support", "work remotely"]

OWNER_HR_QUESTIONS_AND_ANSWER = [
    "What are your strengths and weaknesses?|Strengths: I excel at overcoming new challenges and proactively solving problems with efficiency. I am detail-oriented, highly accurate, and well-organized, with strong documentation and communication skills. I take the initiative in breaking down complex problems into actionable steps and always strive for continuous learning. Weaknesses: I tend to take on too much responsibility myself because I want to ensure everything is done precisely. However, I am working on improving my delegation skills and learning to trust others to share responsibilities effectively. I'm not naturally confident in public speaking or presenting ideas to large groups. To address this, I've been practicing by participating in smaller meetings and preparing more thoroughly for presentations. I sometimes feel impatient when progress is slow, especially when I believe a task could be completed more efficiently. However, I've been working on improving my patience by understanding different working styles and focusing on collaboration to maintain a steady pace"
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
    "Where do you see yourself in five years?|I see myself as a head of data team or being a data consultant, contributing to impactful projects and mentoring others in the field.",
    "What are your salary expectations?|My expectation is competitive with market standards for this role and level of expertise, and I am open to negotiation.",
    "Are you open to travel if the job requires it?|I am open to occasional travel if necessary."
]

OWNER_SOFT_SKILLS = [
                    "Analytical Thinking and Problem-Solving",
                    "Attention to Detail",
                    "Adaptability to Changing Requirements",
                    "Proactive and Self-Motivated",
                    "Effective Time Management and Prioritization",
                    "Collaboration and Teamwork",
                    "Strong Written and Verbal Communication Skills",
                    "Continuous Learning and Self-Improvement",
                    "Empathy and Patience in Conflict Resolution",
                    "Mentorship and Knowledge Sharing"
                    ]

OWNER_CORE_VALUES = [
                    "Integrity and Honesty",
                    "Commitment to Excellence",
                    "Continuous Learning and Growth",
                    "Accountability and Ownership",
                    "Respect for Time and Commitments",
                    "Innovation and Creativity",
                    "Empowering Others Through Data",
                    "Data-Driven Decision Making",
                    "Collaboration and Team Alignment",
                    "Attention to Detail and Precision"
                    ]

OWNER_LEADERSHIP_STYLE = [
                        "Servant Leadership: Focusing on empowering team members to succeed.",
                        "Data-Driven Leadership: Making informed decisions backed by insights.",
                        "Collaborative Leadership: Encouraging open dialogue and input from the team.",
                        "Goal-Oriented Leadership: Setting clear objectives and aligning efforts to achieve them.",
                        "Empathetic Leadership: Understanding team needs and providing support."
                        ]

OWNER_PROBLEM_SOLVING_APPROACH = [
                                "Define and Understand the Problem: Gather all relevant data and context.",
                                "Break Down Complexity: Simplify challenges into manageable steps.",
                                "Data-Driven Analysis: Use analytics to identify patterns, trends, and potential solutions.",
                                "Collaboration: Engage stakeholders to gain insights and diverse perspectives.",
                                "Iterative Improvement: Implement solutions incrementally and refine based on feedback.",
                                "Focus on Root Causes: Address underlying issues to prevent recurrence.",
                                "Documentation and Reflection: Capture learnings to improve future processes."
                                ]

OWNER_COMMUNICATION_STYLE = [
                            "Clear and Concise: Avoids ambiguity and ensures clarity in messaging.",
                            "Collaborative: Promotes open dialogue and encourages feedback.",
                            "Proactive: Keeps stakeholders informed and aligned throughout projects.",
                            "Adaptable: Tailors communication style to the audience and context.",
                            "Transparent: Shares updates and challenges honestly and in a timely manner."
                            ]

OWNER_TEAM_CULTURE_FIT = [
                        "Collaborative and Inclusive Teams",
                        "Commitment to Continuous Improvement",
                        "Innovation and Forward-Thinking Environment",
                        "Respectful and Open Communication",
                        "Focus on Data-Driven Decision Making",
                        "Empowerment and Knowledge Sharing",
                        "Accountability and Ownership in Deliverables",
                        "Supportive and Growth-Oriented Atmosphere"
                        ]

OWNER_EMPLOYER_VALUES = [
                        "Invests in Employee Growth and Development",
                        "Fosters a Culture of Innovation and Learning",
                        "Respects Work-Life Balance",
                        "Encourages Transparent and Open Communication",
                        "Values Data-Driven Decision Making",
                        "Provides Opportunities for Leadership and Impact",
                        "Supports Remote and Flexible Work Options",
                        "Promotes Collaboration and Team Empowerment",
                        "Recognizes and Rewards Excellence"
                        ]
