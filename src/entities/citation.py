class Citation:
    def __init__(self, citation_id, content):
        self.id = citation_id
        self.content = content

    def __str__(self):
        return f"{self.content}"
