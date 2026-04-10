def grade(pred, gt):
    score = 0.0

    if pred.label == gt["label"]:
        score += 0.5

    if pred.action == gt["correct_action"]:
        score += 0.4

    if pred.confidence > 0.7:
        score += 0.1

    return min(score, 1.0)
