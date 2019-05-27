def fields_to_sql_row(fields, table=None):
    filters = []
    for query_filter, value in fields.items():
        if value is None:
            continue
        value = '"{}"'.format(value) if type(value) == str else str(value)
        if table:
            filters.append('{}.{}={}'.format(table, query_filter, value))
        else:
            filters.append('{}={}'.format(query_filter, value))
    return filters
