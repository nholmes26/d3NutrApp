# d3NutrApp

For our final project in COMP790 - Information Visualization, we are utlilizing d3 to create a Nutrition App that tracks macronutrient intake in a manner that is safe for those with eating disorders. <br /><br /> 
- Powered by Flask
- Creates donut charts that track one's progress towards their daily caloric and macronutrient goals
- Users simply select the gender/age option that they fall under, and then enter foods consumed (measured in grams) 
- Unique ability to display progress towards nutritional goals in percentages, rather than specific counts
- This enables intake tracking WITHOUT ever displaying any calorie counts, hopefully preventing potentially triggering effects intake tracking can have on users that have struggled with eating disorders
- For those that do wish to see counts, easy to switch with a simple dropdown in the top right corner
<br /> <br />
Data:

- We obtained recommended intake levels for calories, carbohydrates, fats, and proteins from https://health.gov/our-work/nutrition-physical-activity/dietary-guidelines/previous-dietary-guidelines/2015/advisory-report/appendix-e-3/appendix-e-31a4 <br />
- We have almost 8.8k different foods and their corresponding macronutrient levels, obtained from https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products?resource=download <br />
- Our donut charts were adapted from https://d3-graph-gallery.com/graph/donut_label.html <br />

To run locally:
<br />
- Clone this repo using `git clone git@github.com:nholmes26/d3NutrApp.git`
- Navigate to the d3NutrApp directory in a terminal and run `python app.py` 
<br />
<br />
Debug info:
<br />
- If encountering an access error on Google Chrome despite correctly following the above steps to run locally, try navigating to chrome://net-internals/#sockets and then select 'Flush socket pools'
