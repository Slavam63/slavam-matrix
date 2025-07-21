def adapt_faq(faq_items: list):
    adapted = []
    for q, a in faq_items:
        if "linkedin" in q.lower():
            a += " 🔗 Проверь рекомендации в профиле."
        adapted.append((q, a))
    return adapted
