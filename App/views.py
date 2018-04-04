#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random

from flask import (redirect,
                   render_template,
                   request,
                   url_for,
                   flash)

from App import (app,
                 db_con,
                 models)

app.config["SECRET_KEY"] = '\x87\x1f\x03\xa5\x90\x8c\xacC\x95\xcbB\xe4\xc8\xdb=\x80+\xc3\xd7\x8e\xad\x90\x8f9\x12\x81?\xd4\x82L\xcb\xc1'


@app.route("/")
@app.route("/index/")
def home():
    return render_template("topics/index.html",
                           title="OMAC - Add Topic",
                           posts=db_con.post_store.get_all(),
                           members=db_con.member_store)


@app.route("/topic/add", methods=["GET", "POST"])
def topic_add():
    if request.method == "POST":
        if request.form["submit"] == "Add":
            new_post = models.Post(request.form["topic_title"],
                                   request.form["topic_content"],
                                   member_id=random.randint(1, 3))
            db_con.post_store.add(new_post)
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    else:
        return render_template("topics/topic_add.html",
                               title="OMAC - Add Topic")


@app.route("/topic/delete/<int:id>", methods=["GET", "POST"])
def topic_delete(id):
    post = db_con.post_store.get_by_id(id)
    if request.method == "POST":
        member_id = post.member_id
        if request.form['submit'] == "Delete":
            db_con.post_store.delete(id)
            db_con.update_members_posts()
            return redirect(url_for("my_topics", id=member_id))
        else:
            return redirect(url_for("my_topics", id=member_id))
    return render_template("topics/topic_delete.html",
                           title="OMAC - Delete Topic",
                           post=post)


@app.route("/my_topics/<int:id>")
def my_topics(id):
    member = db_con.member_store.get_by_id(id)
    return render_template("topics/my_topics.html",
                           title="OMAC - My Topics",
                           member=member)
