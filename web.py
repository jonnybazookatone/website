import ads
from flask import Flask, render_template
from flask.ext.cache import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/publications/')
@cache.cached(timeout=24*60*60)
def publications():

    q = ads.SearchQuery(
        q='orcid:0000-0001-8043-4965',
        fl=['bibcode', 'author', 'title', 'citation_count', 'year', 'pub'],
        sort='date desc'
    )
    papers = []
    for paper in q:
        authors = []
        for author in paper.author:
            if 'Elliott' in author:
                authors.append('<b>Elliott, J.</b>')
            else:
                authors.append(author)
        paper.authors = '; '.join(authors)

        papers.append(paper)

    total_citations = sum([paper.citation_count for paper in papers])
    total_publications = len(papers)
    total_publishers = len(set([paper.pub for paper in papers]))

    return render_template(
        'publications.html',
        papers=papers,
        ads_url='https://ui.adsabs.harvard.edu/#abs',
        total_citations=total_citations,
        total_publications=total_publications,
        total_publishers=total_publishers
    )


@app.route('/research/')
def research():
    return render_template('research.html')


@app.route('/software/')
def software():
    return render_template('software.html')


@app.route('/cv/')
def cv():
    return render_template('cv.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
  app.run(debug=True)
