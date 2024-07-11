import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Prasanth")

with col2:
    st.image("images/prasanth.jpg")

st.title(" ")


persona = """
        I am Prasanth T S, a Data Engineer based in Bengaluru with over 2 years of experience in developing and managing data pipelines for enterprise-level projects. I specialize in handling large datasets, improving data processing efficiency, and collaborating with cross-functional teams to deliver scalable solutions.

Contact Information:
Email: prasanthts11@gmail.com
Phone: 9995418907
LinkedIn: Prasanth T S
GitHub: Prasanth-ts
Professional Experience:
Associate Data Engineer at T-Systems ICT India Pvt. Ltd, Bengaluru (Dec 2022 – present)

Led a team to build and test ETL-based data products in AWS for Mercedes Benz.
Migrated 20 years of data from Teradata to AWS, developing data products using PySpark and QLIK.
Improved data processing efficiency by 30% and reduced project delivery time by 20%.
Coordinated with stakeholders to translate business requirements into technical specifications.
Conducted design specification walkthroughs, supported system integration testing, and reduced defects by 20%.
Intern Data Engineer at Datatrained Pvt. Ltd (Feb 2022 – Dec 2022)

Mentored over 200 candidates in live sessions and guided 50+ students to obtain Big Data certificates.
Discussed modules like Big Data, Python, Pyspark, Scala, SQL, and NoSQL.
Data Science and Machine Learning Intern at Innodatatics (Apr 2021 – May 2021)

Created a machine learning algorithm to predict air quality with 89% accuracy.
Developed a YouTube recommendation system using the YouTube API, deployed on AWS EC2.
Skills:
Languages: Python, Pyspark
Big Data Technologies: Apache Spark, Apache Kafka, Hadoop, Hive, Hbase, HDFS, MapReduce
Databases: MySQL, PL/SQL, Cassandra, NoSQL
Cloud Services: AWS (Redshift, Glue, S3, CloudWatch, Athena, Step Machine, IAM, EMR, Lambda), Azure, GCP
Others: Unix shell scripting, Git/GitHub, Pulumi, CI/CD, Machine Learning, Data Modeling
Projects:
Real-Time Data Pipeline for E-Commerce Analytics: Implemented using Apache Kafka and Spark Streaming, reducing data latency from hours to seconds, leading to a 20% increase in conversion rates.
Machine Learning Pipeline for Predictive Maintenance: Reduced unplanned downtime by 30% through early detection of equipment issues.
Customer Sentiment Analysis Platform: Improved customer satisfaction by 18% using NLP techniques to analyze feedback from social media, reviews, and surveys.
Education:
Bachelor of Computer Application (BCA) from Kalinga University, Raipur (2018 – 2021)
Certifications:
Azure Data Fundamentals
Big Data Foundations - Level 2
Spark - Level 1 & Level 2
Databricks Lakehouse Fundamentals
Courses:
Big Data & Data Science from ExcelR
        """

st.title("Prasanth's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

st.write(" ")
st.title("Profile Summary")
st.write("""
I am Prasanth T S, a Data Engineer based in Bengaluru with over 2 years of experience in developing and managing data pipelines for enterprise-level projects. I specialize in handling large datasets, improving data processing efficiency, and collaborating with cross-functional teams to deliver scalable solutions.
""")

st.title("Professional Experience")
st.write("""
**Associate Data Engineer** at T-Systems ICT India Pvt. Ltd, Bengaluru (Dec 2022 – present)
- Led a team to build and test ETL-based data products in AWS for Mercedes Benz.
- Migrated 20 years of data from Teradata to AWS, developing data products using PySpark and QLIK.
- Improved data processing efficiency by 30% and reduced project delivery time by 20%.
- Coordinated with stakeholders to translate business requirements into technical specifications.
- Conducted design specification walkthroughs, supported system integration testing, and reduced defects by 20%.

**Intern Data Engineer** at Datatrained Pvt. Ltd (Feb 2022 – Dec 2022)
- Mentored over 200 candidates in live sessions and guided 50+ students to obtain Big Data certificates.
- Discussed modules like Big Data, Python, Pyspark, Scala, SQL, and NoSQL.

**Data Science and Machine Learning Intern** at Innodatatics (Apr 2021 – May 2021)
- Created a machine learning algorithm to predict air quality with 89% accuracy.
- Developed a YouTube recommendation system using the YouTube API, deployed on AWS EC2.
""")

st.title("Projects")
st.write("""
**Real-Time Data Pipeline for E-Commerce Analytics**
- **Project Description:** Designed and implemented a robust real-time data pipeline using Apache Kafka and Spark Streaming to process and analyze e-commerce transactions, reducing data latency from hours to seconds.
- **Technologies Used:** Apache Kafka, Spark Streaming, AWS S3, Python, SQL
- **Impact:** Enabled real-time insights and decision-making for marketing and sales teams, leading to a 20% increase in conversion rates through timely promotional adjustments.

**Machine Learning Pipeline for Predictive Maintenance**
- **Project Description:** Designed an end-to-end machine learning pipeline to predict system logs in manufacturing plants, integrating data from sensors, maintenance logs, and production records.
- **Technologies Used:** Apache Kafka, Apache Spark, TensorFlow, Python
- **Impact:** Reduced unplanned downtime by 30% through early detection of equipment issues, saving the company significant maintenance costs.

**Customer Sentiment Analysis Platform**
- **Project Description:** Developed a sentiment analysis platform to analyze customer feedback from social media, reviews, and surveys using natural language processing techniques.
- **Technologies Used:** NLP, Python, Apache Spark, Hadoop, Tableau
- **Impact:** Improved customer satisfaction by 18% through early identification and resolution of customer issues, leading to enhanced brand loyalty.
""")

st.title("Education")
st.write("""
**Bachelor of Computer Application (BCA)** from Kalinga University, Raipur (2018 – 2021)
""")

st.title("Certifications")
st.write("""
- Azure Data Fundamentals
- Big Data Foundations - Level 2
- Spark - Level 1 & Level 2
- Databricks Lakehouse Fundamentals
""")

st.title("Skills")
st.write(" ")
st.slider("Programming", 0, 100, 70)
st.slider("Big Data Technologies", 0, 100, 80)
st.slider("Databases", 0, 100, 75)
st.slider("Cloud Services", 0, 100, 85)

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("prasanthts11@gmail.com")


