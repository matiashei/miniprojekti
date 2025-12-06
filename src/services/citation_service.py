class CitationService:
    def __init__(self):
        pass

    def clean_tags(self, tags_string):
        if not tags_string or tags_string.isspace():
            return []

        tags = tags_string.split(",")
        cleaned_tags = []
        for tag in tags:
            cleaned_tag = tag.strip()
            if cleaned_tag:
                cleaned_tags.append(cleaned_tag.lower())
        return list(dict.fromkeys(cleaned_tags))


citation_service = CitationService()
