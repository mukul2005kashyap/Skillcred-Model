from sentence_transformers import SentenceTransformer, util

class AnswerEvaluator:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_similarity(self, correct_answer, user_answer):
        emb1 = self.model.encode(correct_answer, convert_to_tensor=True)
        emb2 = self.model.encode(user_answer, convert_to_tensor=True)

        score = float(util.pytorch_cos_sim(emb1, emb2))
        return round(score * 100, 2)  

