#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools


class BaseStore(object):

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_all(self):
        return (item_instance for item_instance in self._data_provider)

    def get_by_id(self, id):
        instances = self.get_all()
        obj = None
        for item_instance in instances:
            if item_instance.id == id:
                obj = item_instance
                break
        return obj

    def entity_exists(self, item_instance):
        exist = True
        if self.get_by_id(item_instance.id) is None:
            exist = False
        return exist

    def update(self, item_instance):
        all_instances = self.get_all()
        for index, instance in enumerate(all_instances):
            if instance.id == item_instance.id:
                self._data_provider[index] = item_instance
                break

    def delete(self, id):
        item_instance = self.get_by_id(id)
        self._data_provider.remove(item_instance)


class MemberStore(BaseStore):
    """Manipulate the principle operation on members.

    Attributes:
        members (list): Store members objects.
        last_id (int): A counter that holds last added member object id.
    """
    members = []
    last_id = 1

    def __init__(self):
        super(MemberStore, self).__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, name):
        all_members = self.get_all()
        return (member for member in all_members if member.name == name)

    def get_members_with_posts(self, posts):
        """Assign each member to his/her posts

        Args:
            posts (Post): An instance of post class.

        Returns:
            all_members (generator): Updated members generator associated their posts objects.
        """

        all_members = self.get_all()
        for member, post in itertools.product(all_members, posts):
            if post.member_id == member.id and post not in member.posts:
                member.posts.append(post)
        return(member for member in self.get_all())

    def get_top(self):
        """A list top members wrote posts

        Returns:
            all_members (list): Descending sorted ordered list contains top members.
        """
        number_of_top = 2
        all_members = list(self.get_all())
        all_members.sort(key=lambda member: len(member.posts), reverse=True)
        for i in range(number_of_top):
            yield all_members[i]


class PostStore(BaseStore):
    """Manipulate the principle operation on members.

    Attributes:
        posts (list): Store posts objects.
        last_id (int): A counter that holds last added post object id.
    """

    posts = []
    last_id = 1

    def __init__(self):
        super(PostStore, self).__init__(PostStore.posts, PostStore.last_id)

    def get_by_title(self, title):
        all_posts = self.get_all()
        return(post.title for post in all_posts if title in post.title)

    def get_post_by_date(self):
        all_posts = list(self.get_all())
        all_posts.sort(key=lambda post: post.date, reverse=True)
        return (post for post in all_posts)

    def edit_post(self, id, title, body):
        post = self.get_by_id(id)
        post.title = title
        post.body = body
