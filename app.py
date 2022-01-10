from flask import Flask, request, render_template

import utils

app = Flask(__name__)


@app.route('/',)
def page_index():
    posts = utils.get_posts_with_comments_count()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_pk>',)
def page_post(post_pk):

    post = utils.get_post_by_pk(post_pk)
    comments = utils.get_post_comments_by_pk(post_pk)
    comments_count = len(comments)

    return render_template("post.html",
                           post=post,
                           comments=comments,
                           comments_count=comments_count
                           )


app.run()
