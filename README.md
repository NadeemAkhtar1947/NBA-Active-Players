
# NBA Active Players Search App

This app gives all info about NBA active players like name, country, school, draft year, draft round,position, height, weght, player image, etc...
## Documentation

[Documentation](https://linktodocumentation)

Dataset for this project   collected from Kaggle. link of dataset is given below.

https://www.kaggle.com/datasets/szymonjwiak/nba-active-players-data-images?select=players.csv

This dataset consist of two files:-
## a) players.csv 
https://www.kaggle.com/datasets/szymonjwiak/nba-active-players-data-images?select=players.csv
## b) image
https://www.kaggle.com/datasets/szymonjwiak/nba-active-players-data-images?select=img

first, we need to create an image  dataframe i.e df, that contains two columns 'playerid' and 'Filename'. Filename basically keeps the image path.
After creating,   
we will merge both datasets on the basis of playerid. 
data = data.merge(df, left_on='playerid', right_on='playerid')









## Deployment

To deploy this project on local server run

```
  streamlit run app_name(or filename).py
```
To deploy this project on streamlit cloud
please go through this video it better helps.
you will get error on uploading github when you have a file larger than 100MB. To resolve this issue you have to download Git Large File Storage (LFS) that replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com
After downloading, open your Gitbash or command prompt and go to your working directory and then the follow commands one by one:
https://git-lfs.com/

https://www.youtube.com/watch?v=HKoOBiAaHGg


## 🚀 About Me
I'm a Machine Learning Developer...


## Support

For support, email nadeemsdemlde@gmail.com or you may contact me https://portfolionadeem.netlify.app/contact.


## Tech Stack
Programming Languages:

Python: Python is a popular language for data analysis, machine learning, and web development, making it suitable for building recommendation systems.

Data Processing and Analysis:

Pandas: For data manipulation and analysis.
NumPy: For numerical computations.
SciPy: For scientific and technical computing.
Machine Learning Libraries:

Scikit-learn: For building and evaluating machine learning models.

Web Development Frameworks:

Streamlit is an open-source app framework for Machine Learning and Data Science teams. 

Data Visualization:

Matplotlib: For creating static visualizations.
Seaborn: For statistical data visualization.
Plotly: For creating interactive and dynamic visualizations.

Deployment:

Streamlit Cloud: For hosting the web application and model deployment.

Version Control:

Git: For version control and collaboration.

APIs:


Text Preprocessing:

NLTK: For natural language processing tasks.

Development Environment:

Jupyter Notebook, PyCharm.

