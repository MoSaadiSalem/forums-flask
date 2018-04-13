#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import (redirect,
                   render_template,
                   request,
                   url_for,
                   jsonify)

from App import (app,
                 db_con,
                 models)

app.config[
    "SECRET_KEY"] = '\x87\x1f\x03\xa5\x90\x8c\xacC\x95\xcbB\xe4\xc8\xdb=\x80+\xc3\xd7\x8e\xad\x90\x8f9\x12\x81?\xd4\x82L\xcb\xc1'


@app.route("/")
@app.route("/index/")
def home():
    return render_template("topics/index.html",
                           title="OMAC - Add Topic",
                           posts=db_con.post_store.get_post_by_date(),
                           members=db_con.member_store)


@app.route("/topic/add/<int:member_id>", methods=["GET", "POST"])
def topic_add(member_id):
    if request.method == "POST":
        if request.form["submit"] == "Add":
            new_post = models.Post(request.form["topic_title"],
                                   request.form["topic_content"],
                                   member_id)
            db_con.post_store.add(new_post)
            db_con.update_members_posts()
            return redirect(url_for("my_topics", member_id=member_id))
        else:
            return redirect(url_for("my_topics", member_id=member_id))
    else:
        return render_template("topics/topic_add.html",
                               title="OMAC - Add Topic",
                               member_id=member_id)


@app.route("/topic/edit/<int:post_id>", methods=["GET", "POST"])
def topic_edit(post_id):
    post = db_con.post_store.get_by_id(post_id)

    if request.method == "POST":
        if request.form["submit"] == "Save":
            db_con.post_store.edit_post(post.id,
                                        request.form["topic_title"],
                                        request.form["topic_content"])

            return redirect(url_for("my_topics", member_id=post.member_id))
        else:
            return redirect(url_for("my_topics", member_id=post.member_id))
    else:
        return render_template("topics/topic_edit.html",
                               title="OMAC - Edit Topic",
                               post=post)


@app.route("/topic/view/<int:post_id>")
def topic_view(post_id):
    post = db_con.post_store.get_by_id(post_id)
    member_name = db_con.member_store.get_by_id(post.member_id).name
    return render_template("topics/topic_view.html",
                           title="OMAC - View Topic",
                           post=post,
                           member_name=member_name)


@app.route("/topic/delete/<int:post_id>", methods=["GET", "POST"])
def topic_delete(post_id):
    post = db_con.post_store.get_by_id(post_id)
    if request.method == "POST":
        member_id = post.member_id
        if request.form['submit'] == "Delete":
            # To remove posts from memory till connect to database
            # the following 2 lines are temporary
            member = db_con.member_store.get_by_id(post.member_id)
            member.posts.remove(post)
            # temp lines end here

            db_con.post_store.delete(post_id)
            db_con.update_members_posts()
            return redirect(url_for("my_topics", member_id=member_id))
        else:
            return redirect(url_for("my_topics", member_id=member_id))
    return render_template("topics/topic_delete.html",
                           title="OMAC - Delete Topic",
                           post=post)


@app.route("/my_topics/<int:member_id>")
def my_topics(member_id):
    member = db_con.member_store.get_by_id(member_id)
    return render_template("topics/my_topics.html",
                           title="OMAC - My Topics",
                           member=member,
                           posts_no=len(member.posts))


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__ for post in db_con.post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods=["POST"])
def topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["body"], request_data["member_id"])
    db_con.post_store.add(new_post)
    return jsonify(new_post.__dict__)
