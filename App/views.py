#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random

from flask import (redirect,
                   render_template,
                   request,
                   url_for)

from App import (app,
                 db_con,
                 models)


@app.route("/")
@app.route("/index/")
def home():
    title = "OMAC - All Topics"
    return render_template("index.html",
                           title=title,
                           posts=db_con.post_store.get_all(),
                           members=db_con.member_store)


@app.route("/topic/add", methods=["GET", "POST"])
def add_topic():
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
        title = "OMAC - Add Topic"
        return render_template("add_topic.html", title=title)
