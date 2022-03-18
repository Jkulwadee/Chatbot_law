from django.apps import AppConfig
import pathlib
import pandas
import pickle


class BotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bot"
    classifier = None
    responses = None

    def load_data(self):
        # print('load data')
        path = pathlib.Path(__file__).parent.parent

        dfs = pandas.read_excel(path / "data/response_law.xlsx")

        responses = {}
        for df in dfs.to_dict("records"):
            if df["tag"] not in responses:
                responses[df["tag"]] = []
            responses[df["tag"]].append(df["response"])

        f = open(path / "data/my_classifier.pickle", "rb")
        classifier = pickle.load(f)
        f.close()
        return classifier, responses

    def ready(self):
        print("ready")
        self.classifier, self.responses = self.load_data()
