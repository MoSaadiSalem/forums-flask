#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from App import models

dummy_members = [
    models.Member("Mohammed", 20),
    models.Member("Ahmed", 22),
    models.Member("Abdo", 25),
]

dummy_posts = [
    models.Post("Agriculture", "Agriculture is amazing", 1),
    models.Post("Engineering", "I love engineering", 1),

    models.Post("Medicine", "Medicine is great", 2),
    models.Post("Architecture", "Spectacular art", 2),
    models.Post("Astronomy", "Space is awesome", 2),

    models.Post("Geology", "Earth is our friend", 3),
    models.Post("ComputerSci", "Our passion", 3),
    models.Post("Algorithms", "Yeah, more of that", 3),
    models.Post("Operating Systems", "Ewww", 3),
]


def seed_stores(member_store, post_store):
    for member in dummy_members:
        member_store.add(member)
        print "## Debug Member ID: ", member_store.members[-1].id

    for post in dummy_posts:
        post_store.add(post)
        print "## Debug Post Member ID:", post_store.posts[-1].member_id
