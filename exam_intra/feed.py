import string
import random
import pathlib
import time

class Feed:
    PATH_FILE = pathlib.Path(__file__).parent.joinpath("data.txt")

    def __init__(self, model, name="BMW") -> None:
        self.model = model
        self.name = name
        self.alphabet = str(string.ascii_lowercase)

    def getResult(self):
        self.name = "".join([i for i in self.name if i.isalpha()])
        if self.model == "index":
            return "".join([str(self.alphabet.index(i.lower())) for i in self.name])
        if self.model == "merge":
            return self.name.upper()+str(len(self.name))

    def getMix(self, limit):
        random_letter = str("".join([random.choice(self.alphabet) for i in range(limit)]))
        self.name = str(random_letter)+self.getResult()
        return self.name

    def save(self):
        dt = str({"name": self.name})
        with open(Feed.PATH_FILE, mode="w") as file:
            file.write(dt)

class CustomFeed(Feed):
    def __init__(self, model, name="BMW") -> None:
        super().__init__(model, name)

    def getMix(self, limit):
        rezilta = super().getMix(limit)
        start = time.time()
        end_time = time.time()
        print(f"Repons metòd la se {rezilta}, Li ekzekite pandan {end_time - start} sec")


feed = Feed("index", "ESIH")
# feed = Feed("merge", "ESIH")
print(feed.getResult())
print(feed.getMix(12))
feed.save()

print("")
d = CustomFeed("merge", "alo alo")
d.getMix(7)