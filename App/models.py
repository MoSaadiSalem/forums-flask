#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import datetime


class Member(object):
    """Member related information

    Attributes:
        id (int): A unique member id.
        posts (list): List of posts id created by the member.

    """

    def __init__(self, name, age):
        """Create a new member

        Args:
            name (str): Member name.
            age (int): Member age.
        """

        self.name = name
        self.age = age
        self.id = 0
        self.posts = []

    @property
    def __str__(self):
        return "Name: %s\nAge: %d\nMember ID: %s\nPosts:%s " % (self.name, self.age, self.id, len(self.posts))

    @property
    def __dict__(self):
        return {"id": self.id,
                "name": self.name,
                "age": self.age,
                "posts": self.posts,
                }


class Post(object):
    """Post related information

    Attributes:
        id (int): A unique post id.
    """

    def __init__(self, title, body, member_id):
        """Create a new post

        Args:
            title (str): Post title.
            body (str): Post content.
            member_id (int): Member id who is the creator of the post.
        """

        self.title = title
        self.body = body
        self.member_id = member_id
        self.id = 0
        self.date = datetime.datetime.now()

    @property
    def __str__(self):
        return "Title: %s\nContent: %s\nMember ID: %d\nPost ID: %d\nDate/Time: %s" % (
            self.title, self.body, self.member_id, self.id, self.date.strftime("%a %d-%m-%Y %H:%M:%S"))

    @property
    def __dict__(self):
        return {"id": self.id,
                "title": self.title,
                "body": self.body,
                "member_id": self.member_id,
                }
