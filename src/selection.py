def filter_data(data, filters):
    """
    Filters data based on given conditions.
    :param data: List of dictionaries (JSON objects)
    :param filters: Dictionary of filter conditions
    :return: Filtered list of dictionaries
    """
    def _match_filter(item, field, value):
        """
        Helper function to check if a filter matches a nested field in the item.
        :param item: Dictionary representing a review, comment, or post
        :param field: Nested field to check (e.g., "user_info.age_group")
        :param value: Expected value
        :return: True if the filter matches, False otherwise
        """
        keys = field.split(".")
        current = item
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return False
        return value in str(current)

    filtered_data = []
    for record in data:
        if record.get("source", "").startswith("amazon"):
            # Handle Amazon reviews
            reviews = record.get("reviews", [])
            filtered_reviews = [
                review for review in reviews
                if all(_match_filter(review, key, value) for key, value in filters.items())
            ]
            if filtered_reviews:
                record["reviews"] = filtered_reviews
                filtered_data.append(record)
        elif record.get("source", "").startswith("reddit"):
            # Handle Reddit posts
            comments = record.get("comments", [])
            filtered_comments = [
                comment for comment in comments
                if all(_match_filter(comment, key, value) for key, value in filters.items())
            ]
            if filtered_comments:
                record["comments"] = filtered_comments
                filtered_data.append(record)
        elif record.get("source", "").startswith("youtube"):
            # Handle YouTube comments
            comments = record.get("comments", [])
            filtered_comments = [
                comment for comment in comments
                if all(_match_filter(comment, key, value) for key, value in filters.items())
            ]
            if filtered_comments:
                record["comments"] = filtered_comments
                filtered_data.append(record)
    return filtered_data
