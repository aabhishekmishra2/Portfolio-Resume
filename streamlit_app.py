import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Abhishek Mishra, Data Scientist.
##### *Resume*  
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I'm Data scientist with a master's degree in data science, specializing in advanced analytical techniques and machine learning to extract actionable insights and support data-driven decision-making. 
- Passionate about coding, problem-solving, and continuously advancing expertise through research to tackle complex challenges.
- Adept at leveraging cutting-edge research in advanced analytics and machine learning to drive innovation and support data-driven strategies.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000000;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/abhishek-mishra-917b0a234/" target="_blank">Abhishek Mishra</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Project Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Data Science), *Chennai Mathematical Institute*, India',
'2022-2024')
st.markdown('''
- GPA: `3.7`
- Relevant Coursework : Machine Learning, Deep Learning, Linear Algebra, Design and Analysis of Algorithms, NLP, Database Management and SQL 
- Passed with First Class Honors.
- <span style="font-weight: bold; font-family: Arial, sans-serif; color: #00000,font-size: 0.2em;">Major Project</span>:  Developed and implemented advanced execution algorithms for real-time algorithmic trading in volatile markets, reducing market impact costs by 20-30%. Improved VWAP efficiency by over 10% using Almgren-Chriss and Konishi algorithms, achieving execution prices within 0.03% of market VWAP across various order sizes. Enhanced trading efficiency through dynamic strategy adjustments based on real-time market conditions.
''',unsafe_allow_html=True)

txt('**Bachelors of Science** (Statistics), *Banaras Hindu University*, India',
'2019-2022')
st.markdown('''
- GPA: `4`
- Relevant Coursework: Statistical Analysis, Population Statistics, Sampling Techniques and Statistical Inference. 
- Graduated with First Class Honors.
- <span style="font-weight: bold; font-family: Arial, sans-serif; color: #00000,font-size: 0.2em;">Major Project</span>: Conducted an in-depth analysis of population statistics utilizing a variety of sampling techniques to examine public preferences regarding sector selection. The study explored individuals' behavioral tendencies and inclinations toward public versus private sectors across multiple parameters.
''',unsafe_allow_html=True)

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist |** o9 Solutions Management India Private Limited, Bangalore, India',
'2024-Present')
st.markdown('''
- Maintained and updated existing machine learning models to adapt to changing business needs and data patterns
- Developed and maintained scalable data pipelines and ETL processes using PySpark for processing large datasets.
- Implemented and optimized time series forecasting models to enhance predictive analytics and business decision-making.
- Leveraged advanced statistical and machine learning techniques to develop innovative solutions for complex business problems.
- Created comprehensive documentation and reports to communicate analytical findings and model performance to stakeholders.
''')

txt('**Industry Project |** Instructor- Dr Priyavrat Deshpandey & Koushik Krishnan, CMI, India',
'Jan-April (2024)')

st.markdown('''
- Utilized high-frequency snapshot data for real-time algorithmic trading in volatile markets.
- Developed  execution algorithms, resulting in a `20-30\%` reduction in market impact costs.
- Achieved optimal trading efficiency by dynamically adjusting strategies based on real-time market conditions.
- Improved VWAP  efficiency by over `10%` using Almgren-Chriss and Konishi algorithms compared to baseline models
- Achieved execution prices within `0.03%` of market VWAP across (1000, 5000, and 10000 units) order sizes
''')
txt('**Data Science Intern**, MirrAR Innovation Technology Private Limited, Chennai',
'May-Aug (2023)')
st.markdown('''
- Developed a conversational chatbot using Google’s Dialogflow platform
- Designed and implemented an interactive dialogue system for seamless user interaction.
- Integrated the chatbot with a robust backend SQL database for efficient data management.
- Demonstrated expertise in conversation management and real-time data retrieval
- Utilized advanced natural language understanding (NLU) capabilities to enhance chatbot performance.
''')


# txt('**Lecturer**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2006-2009')
# st.markdown('''
# - Provided mentorship and supervision to junior faculty, researchers, Ph.D./M.Sc./B.Sc. students. Mentored `3` Post-doctoral fellows, supervised `13` Ph.D. students, supervised `8` M.Sc. students, supervised `13` B.Sc. students and hosted `6` visiting students from U.S., Sweden and India.
# - Wrote and applied for research grants. Served as Principal Investigator for research grants that have been awarded `12.5 million THB` and `1.117 million SEK` in research funding from Thai and Swedish grant agencies.
# - Conducted research by applying machine learning to computational drug discovery and ensuring that research output exceeds `20+` articles per year.
# - Taught `10+` undergraduate/graduate classes on Bioinformatics, Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
# - Peer reviewed `100+` research articles for leading scientific journals.
# ''')
#
# txt('**Co-Chair**, International Conference on Pharmaceutical Bioinformatics at Pattaya, Thailand',
# '2016')
# st.markdown('''
# - Oversee all aspects of the conference preparations from conception to launch. This include inviting keynote and plenary speakers, create advertisement flyers, create abstract book, etc.
# - Conference attracted `200+` participants from `40+` countries from university and industry sector.
# - Chaired keynote session, technical workshop and some of the parallel sessions.
# ''')
#
# txt('**Content Creator**, [Data Professor YouTube Channel](https://youtube.com/dataprofessor/)',
# '2019-Present')
# st.markdown('''
# - `100,000+` subscribers on YouTube
# - Created `261` educational videos on data science, machine learning and bioinformatics as well as hosted several podcast episodes with data scientists.
# - Created `3` sponsored videos for Notion, Gradio and Classpert.
# ''')
#
# txt('**Content Creator**, [Coding Professor YouTube Channel](https://youtube.com/codingprofessor/)',
# '2019-Present')
# st.markdown('''
# - `3,200+` subscribers on YouTube
# - Created `38` educational videos on Python and R programming.
# ''')
#
# txt('**Technical Writer**, [Data Professor Blog](https://data-professor.medium.com/) on Medium.com',
# '2019-Present')
# st.markdown('''
# - `4,100+` subscribers on Medium
# - Written `68` technical blogs on data science, machine learning and bioinformatics.
# ''')

#####################
st.markdown('''
## Self Project Portfolio
''')
txt4('Transfer Learning', 'Fine tune Pretrained Model for Classification Task', 'https://github.com/aabhishekmishra2/Transfer-Learning')
txt4('Encoder-Decoder', 'An automated data mining software based on Weka', '')
txt4('Deployment', 'Flask application with Docker containerization and continuous integration','https://github.com/aabhishekmishra2/Flask-App-Dockerization-and-Continuous-Integration')
txt4('Spam Classification', 'Used Various Machine Learning Models for Spam Classification', 'https://github.com/aabhishekmishra2/Spam-Classification')
txt4('Shiny DashBoard', 'Deploy R shiny Dashboard to Visualize various aspect for food productions','https://github.com/aabhishekmishra2/Food-Production-India-Dashboard')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Problem Solving','`DataStructure and Algorithms`' )
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `PySpark`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`,`PyTorch`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Git`, `R Shiny`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/abhishek-mishra-917b0a234/')
txt2('Twitter', 'https://twitter.com/mishraabhi1430')
txt2('GitHub', 'https://github.com/aabhishekmishra2')
txt2('LeetCode', 'https://leetcode.com/u/aabhishekmishra/')
