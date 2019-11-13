# this-hackathon-project-isnt-real

## About

This is a [hackathon](https://en.wikipedia.org/wiki/Hackathon) project
for [Hack UTD VI](https://hackutd-vi.devpost.com).

At hackathons, you submit what is called a devpost at the end. it is
basically a short blog post about what you did, why you did it, what
technologies you used, etc. This project scraped a bunch of old
devposts and used some machine learning to predict if a future project
will be a winner, and also generate new fake hackathon projects.

### Authors

- [Elise Renwick](https://github.com/eliserenwick)
- [Caleb Rotello](https://caleb.rotello.dev)
- [Dagny Stahl](https://github.com/dagnystahl)
- [Jake Vossen](https://jake.vossen.dev)

### Running

Running is just running the `site.py` file in `generate-text`
directory with Python 3. That will start a local server on port 80 in
dev mode. You will need some Python dependencies which can be
installed with `pip3`, such as `beautifulsoup4`, `flask`,
`wtforms`, `numpy`, `scikit-learn`, and `matplotlib`. You can then navigate to `localhost` for the randomly
generated posts, and `localhost/predict` to enter the title of a
devpost to predict the title.

### Brief Technical Description

Like all hackathon projects, everything is thrown together quickly and
is a bit of a mess. We didn't always follow best practices with git
and such, so there are definitely messes left around. Also, the sites
are not generated as you refresh, rather pull from a pre-compiled list
of data we created using [gpt2](https://github.com/openai/gpt-2).

## Devpost

### Inspiration
N/A

### What it does
Generates a devpost for a hackathon project, and predicts if a project
is a winner based on its devpost.

### How I built it
First, we explored text generation by forcing a bot to read all of
Twilight, and then rewrite its own version. Meanwhile, Jake the data
fairy scraped all the most popular devposts from devpost.com, using
the Python and `BeautifulSoup`. Once the bot could write with the same
suspenseful elegance of Stephanie Meyers, we decided it was ready to
take on the devposts. Our text generating/sass department used
`gpt-2-simple` and ignored how little sense the results made.

### Challenges I ran into
Creating the model to classify a project was rough. After extensive
data analysis, we came to the conclusion that there is a minimal
correlation between any quantitative data that can be pulled from a
devpost and the project's success. So that is a fat our bad. The
prediction algorithm will classify a project with the same accuracy as
that of a slightly more insightful coin. Someone kept moving things
around in the git repo and Jake forgot his glasses. Also our bot got waaaaay too political.

#### Accomplishments that I'm proud of
- Successfully implemented k-nearest neighbors
- Generated adequately coherent text
- Had some good yucks

### What I learned
- There is NOT enough coconut water to go around
- The quality of a devpost is entirely subjective ;)
- Jeb Bush was in prison for 30 years

### What's next for This Hackathon Project is Not Real
- We plan to continue by creating random manifesto generators and exploring writing our own novels by training our bot on individual author’s styles.
