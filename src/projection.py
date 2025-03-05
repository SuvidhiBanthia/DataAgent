def project_data(data, fields):
    """
    Projects only the specified fields from the data.
    :param data: List of dictionaries (JSON objects)
    :param fields: List of fields to include
    :return: Projected list of dictionaries
    """
    projected_data = []
    for record in data:
        if record.get("source", "").startswith("amazon"):
            # Handle Amazon reviews
            projected_record = {field: record[field] for field in fields if field in record}
            projected_record["reviews"] = [
                {field: review[field] for field in fields if field in review}
                for review in record.get("reviews", [])
            ]
            projected_data.append(projected_record)
        elif record.get("source", "").startswith("reddit"):
            # Handle Reddit posts
            projected_record = {field: record[field] for field in fields if field in record}
            projected_record["comments"] = [
                {field: comment[field] for field in fields if field in comment}
                for comment in record.get("comments", [])
            ]
            projected_data.append(projected_record)
        elif record.get("source", "").startswith("youtube"):
            # Handle YouTube comments
            projected_record = {field: record[field] for field in fields if field in record}
            projected_record["comments"] = [
                {field: comment[field] for field in fields if field in comment}
                for comment in record.get("comments", [])
            ]
            projected_data.append(projected_record)
    return projected_data