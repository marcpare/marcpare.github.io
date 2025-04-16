import mistune
from flask import Flask, render_template, url_for
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

class MyMarkdownRenderer(mistune.HTMLRenderer):
    def image(self, alt, url, title=None):

        # Parse out any query params from the url using urllib.parse
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        width = query_params.get("w")

        # Remove the query params from the url
        url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))

        # For localhost, point to the static directory
        full_url = url_for('static', filename=url)

        # TODO: implement image url for github io build

        attrs = {
            "src": full_url,
            "alt": alt,
            "title": title
        }

        if width:
            width = width[0]
            attrs["width"] = width

        # Build the imag tag from the attrs dict
        img_tag = f'<img {" ".join([f"{k}=\"{v}\"" for k, v in attrs.items()])} />'
        
        return img_tag

@app.route('/articles/<article_name>')
def article(article_name):
    
    markdown_filename = f'articles/{article_name}.md'
    with open(markdown_filename, 'r') as file:
        markdown_content = file.read()  

    # convert markdown to html
    markdown = mistune.create_markdown(renderer=MyMarkdownRenderer(escape=False), plugins=["table"])
    html_content = markdown(markdown_content)

    print(html_content)

    return render_template('markdown_article.html', markdown_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)
