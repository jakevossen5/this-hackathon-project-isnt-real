# this-hackathon-project-isnt-real

## Inspiration
Lack of inspiration

## What it does
Generates a dev post for a hackathon project, and predicts if a project is a winner based off its dev post.

## How I built it
First, we explored text generation by forcing a bot to read all of Twilight, and then rewrite its own version. Meanwhile, Jake the data fairy scraped all the most popular dev posts from devpost.com, using the requests python library and BeautifulSoup. Once the bot could write with the same suspensful elegance of Stephanie Meyers, we decided it was ready to take on the dev posts. Our text generating/sass department used textgenrnn and had to tweak the model to fit the specific text data.

## Challenges I ran into
Creating the model to classify a project was rough. After extensive data analysis, we came to the conclusion that there is minimal correlation between any quantative data that can be pulled from a dev post and the project's success. So that is a fat our bad. The prediction algorithm will classify a project with the same accuracy as that of a slighlty more insightful coin. Someone kept moving things around in the git repo and Jake forgot his glasses.

## Accomplishments that I'm proud of
-Succesfully implemented k-nearest neighbors
-Generated adequately coherent text
-Had some good yucks


## What I learned
-There is NOT enough coconut water to go around

## What's next for This Hackathon Project is Not Real
