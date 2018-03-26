#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import dummy_data
import stores

member_store = stores.MemberStore()
post_store = stores.PostStore()

dummy_data.seed_stores(member_store, post_store)
