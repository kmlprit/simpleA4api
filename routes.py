from middleware import db, index, user_profile
from flask import jsonify


def initialise_routes(app):
    if app:
        app.add_url_rule('/api/hello/', 'index', index)
        app.add_url_rule('/api/db/', 'db', db)
        app.add_url_rule('/api/', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        app.add_url_rule('/api/profile/<id>', 'user_profile', user_profile)
    return None


def list_routes(app):
    for route in app.url_map.iter_rules():
        print(route)
        print(route.endpoint)
        print(route.methods)
    return "Routes Info"


def list_routes(app):
    routes = []
    for route in app.url_map.iter_rules():
        routes.append({'Route': str(route),
                       'Endpoint': route.endpoint,
                       'Methods': list(route.methods)})
    return jsonify({"Routes": routes, "Total": len(routes)})
