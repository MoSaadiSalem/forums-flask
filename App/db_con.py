#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import dummy_data
import stores

member_store = stores.MemberStore()
post_store = stores.PostStore()

dummy_data.seed_stores(member_store, post_store)


def update_members_posts():
    member_store.get_members_with_posts(post_store.posts)


update_members_posts()
