import streamlit as st
from PIL import Image


# Apply css format
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Ilia Gouaref
''')

# Import banner
image = Image.open('Banner.jpg')
st.image(image, width=705)
# Banner link "https://pixabay.com/illustrations/ai-artificial-intelligence-6767501/"

st.write('''
# Data Scientist
''')

# Contacts
col0, col1, col2, col3 = st.columns([0.6,1,1,1])

col0.write(" ")
col1.markdown("[![mail](https://img.icons8.com/ios-filled/48/000000/email-sign.png)](mailto:gouaref.ilia@gmail.com)")
col2.markdown("[![linkedin](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/ilia-gouaref/)")
col3.markdown("[![github](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/Iliato)")


#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #008080;">
  <a class="navbar-brand" href="" target="_blank">Ilia GOUAREF</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#ilia-gouaref">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#tools">Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#publications">Publications</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)




#st.markdown('## Summary', unsafe_allow_html=True)

# st.info('''
#* Trained as an engineer in economics and applied statistics, I have six years of experience in data analysis as a research assistant. 
#* I have been attracted by digital sciences and succeeded in becoming a Data Scientist this year. 
#* I am looking for opportunities to develop digital solutions for the optimisation of industrial and societal challenges.
#''')


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  

#####################
st.markdown('''
## Education
''')

txt('**Data Scientist** (Certification Paris La Sorbonne), *Datascientest*, Paris',
'2021')
st.markdown('''
- Python programming, Data Visualisation, Machine Learning, BigData, Deep Learning, Reinforcement Learning
''')

txt('**Master Econometrics** , *Aix-Marseille School of Economics*, Marseille',
'2013-2014')
st.markdown('''
- Econometrics of linear and non-linear models, Time Series Analysis, Non-parametric Models, R and Stata programming
''')

txt('**Engineer in Economics and Applied Statistics** , *ENSSEA*, Algiers',
'2008-2013')
st.markdown('''
- Economics, Statistics, Game Theory, Computer science.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist (Intern)**, [Akanthas](https://www.akanthas.com/), France',
 '2021')
st.markdown('''
- Creation and development of data visualization tools and AI models in the industrial waste management sector (NDA)
''')

txt('**Research and Teaching Assistant (ATER)**, UEVE, IDF, France',
'2018-2019')
st.markdown('''
- Research: Applied Econometric to public policy evaluation.
- Teaching: Macroeconomics, Statistics
''')
txt('**Phd Candidate, ATER**, Aix-Marseille University, Marseille, France',
'2014-2018')
st.markdown('''
- Research : Applied econometric study of non Take-Up of welfare benefits. 
- Participation to international conferences.
- Teaching: Microeconomics, Econometrics (Master level)
''')

#####################
st.markdown('''
## Tools
''')
txt2('Programming', '`Python`, `R`')
txt2('Data processing', '`pandas`, `numpy`, `SQL`')
txt2('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `bokeh`, `ggplot2`')
txt2('Machine Learning', '`scikit-learn`')
txt2('Deep Learning', '`TensorFlow`, `keras`')
txt2('Image processing', '`OpenCV`')
#txt2('Web development', '`Flask`, `HTML`, `CSS`')
txt2('Model deployment', '`streamlit`, `Heroku`')
txt2('Version control', '`Git`, `GitHub`')
txt2('Writing', '`Latex`, `Google docs`, `MS Office`')
txt2('Project Managment', '`Notion`')

#####################
st.markdown('''
## Skills
''')

txt('**Data cleaning and processing.** ',' ')
st.markdown('''
- Remove duplicate, irrelevant or outlier observations
- Fix structural errors
- Missing data dilema (drop, replace or ignore)
''')

txt('**Implement advanced concepts in Statistics and Machine Learning.** ',' ')
st.markdown('''
- Hypothesis Testing
- Regression (Linear, Logistic, Time series forecasting)
- Dimension reduction (PCA)
- Supervised classifiction (KNN, Random Forest)
- Clustering (K-Means, Hierarchical clustering)
''')

txt('**Implement object detection models and classification (deep learning).** ',' ')
st.markdown('''
- Convolutional neural networks (CNN)
- Recurrent neural networks (RNN)
- You Only Look Once (YOLO)
''')

txt('**Develop a web application associated with a project.** ',' ')
st.markdown('''
- Streamlit wab application to deploy on streamlit sharing or heroku
''')

#####################
st.markdown('''
## Publications
''')
txt('**[Does information on pensions change the employement decisons of seniors in France?](https://www.cairn.info/revue-francaise-d-economie-2020-3-page-43.htm)**, Kadija Charni and Ilia Gouaref, Revue française d’économie, 2021/3 (Janvier – Vol. XXXV)', '2021')
