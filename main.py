#!/usr/bin/env python
import webapp2
from handlers.base import CookieAlertHandler, MainHandler
from handlers.topics import TopicAdd, TopicDetailsHandler, TitleTopicHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic-details', TopicDetailsHandler, name="topic-details"),
    webapp2.Route('/title', TitleTopicHandler, name="title"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
], debug=True)

