### Movie Recommendation System

### Overview
This project is a Machine Learning-based Movie Recommendation System that suggests movies based on similarity between films. It analyzes features such as genre, cast, keywords, and overview to generate personalized recommendations.


### Features
- Content-based filtering using movie metadata  
- Cosine similarity to measure similarity between movies  
- Integration with TMDb API to display movie posters  
- Explanation for each recommendation  
- Interactive web interface using Streamlit  


### How It Works
The system processes movie data and combines important features such as genres, cast, keywords, and descriptions into a single representation.  
This data is then converted into numerical vectors using text vectorization techniques.  
Cosine similarity is applied to find relationships between movies, and the top similar movies are recommended to the user.


### Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Requests (for API integration)  



### Project Structure
Algonive_Movie_Recommendation/

 data/
 main.py
 app.py
 movies.pkl
 similarity.pkl
 requirements.txt
 README.md


### Installation and Setup

1. Clone the repository:
git clone <your-repo-link>  
cd Algonive_Movie_Recommendation  

2. Create and activate virtual environment:
python -m venv venv  
venv\Scripts\activate  

3. Install dependencies:
pip install -r requirements.txt  

4. Run preprocessing script:
python main.py  

5. Run the application:
streamlit run app.py  



### Usage
- Select a movie from the dropdown menu  
- Click on the "Recommend" button  
- The system will display top recommended movies along with posters and explanations  



### Future Improvements
- Full implementation of collaborative filtering  
- Integration of real user reviews for sentiment analysis  
- Enhanced recommendation accuracy using hybrid models  
- Improved UI/UX design  


### Acknowledgment
This project was developed as part of the Machine Learning Internship at Algonive.
