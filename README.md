# d3NutrApp

For our final project in COMP790 - Information Visualization, we are utlilizing d3 to create a Nutrition App that tracks macronutrient intake. <br /><br /> 
This app, powered by Flask, creates donut charts that track one's progress towards their daily caloric and macronutrient goals (g). All you need to do is select the gender/age option that you fall under, and then start entering foods along with the amount you consume (g)!

- We obtained recommended intake levels for calories, carbohydrates, fats, and proteins from https://health.gov/our-work/nutrition-physical-activity/dietary-guidelines/previous-dietary-guidelines/2015/advisory-report/appendix-e-3/appendix-e-31a4 <br />
- We have almost 8.8k different foods and their corresponding macronutrient levels per serving, obtained from https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products?resource=download <br />
- Our donut charts were adapted from https://d3-graph-gallery.com/graph/donut_label.html <br />

To run locally:
<br />
- Clone this repo using `git clone git@github.com:nholmes26/d3NutrApp.git`
- Navigate to the directory in a terminal and run `python app.py` 
