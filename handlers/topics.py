from handlers.base import BaseHandler
from google.appengine.api import users
from models.topic import Topic

class TopicAdd(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        title = self.request.get("title")
        text = self.request.get("text")

        new_topic = Topic(title=title, content=text, author_email=user.email())
        new_topic.put()  # put() saves the object in Datastore

        return self.redirect_to("topic-details")

class TopicDetailsHandler(BaseHandler):
    def get(self):
        new_topic = Topic.query().fetch()
        params = {"Topic": new_topic}
        return self.render_template("topic_details.html", params=params)


class TitleTopicHandler(BaseHandler):
    def get(self):
        sporocilo = Topic.query().fetch()
        params = {"Topic": sporocilo}
        return self.render_template("title.html", params=params)