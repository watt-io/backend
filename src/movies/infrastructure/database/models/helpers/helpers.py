from datetime import datetime


def generate_data(mapper, connection, instance):
    instance.created_at = datetime.now()