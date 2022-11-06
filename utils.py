import json


def load_candidates(file):
    """загрузим данные из файла"""
    with open(file, 'r') as file:
        return json.load(file)


def get_all(candidates):
    """
    покажем всех кандидатов
    Закинем всех кадидатов в список:Имя,Позиция,Скилл
    """
    all_candidates = []
    for candidate in candidates:
        all_candidates.append(candidate["name"])
        all_candidates.append(candidate["position"])
        all_candidates.append(candidate["skills"])
    return all_candidates


def get_by_pk(pk, candidates):
    """вернет кандидата по pk"""
    for candidate in candidates:
        if candidate["pk"] == pk:
            """возвращаем кандидата по позиции Фото,Имя,Позиция,Скилл"""
            return f"<img src='{candidate['picture']}"
            return f"<pre>{candidate['name']}"
            return f"{candidate['position']}"
            return f"{candidate['skills']}"


def get_by_skill(skill_name, candidates):
    """вернет кандидатов по навыку"""
    candidate_with_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            candidate_with_skill.append(candidate["name"])
            candidate_with_skill.append(candidate["position"])
            candidate_with_skill.append(candidate["skills"])
            candidate_with_skill.append('\n')
    return "<pre>" + "\n".join(candidate_with_skill) + "</pre>"
