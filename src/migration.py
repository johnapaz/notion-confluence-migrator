def migrate_content(notion_api, confluence_api, database_id, space_key):
    notion_content = notion_api.get_content(database_id)
    # Transform notion_content into Confluence format
    confluence_content = "<p>Sample Content</p>"  # Replace with actual transformation logic
    response = confluence_api.create_page(space_key, "Migrated Page", confluence_content)
    return response
