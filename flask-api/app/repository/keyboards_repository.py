from ..models.keyboards import Keyboards, keyboard_schema, keyboards_schema
from app import db


def save(keyboard: Keyboards):
    try:
        db.session.add(keyboard)
        db.session.commit()
        return keyboard_schema.dump(keyboard)

    except Exception as e:
        db.session.rollback()
        raise e


def delete(keyboard: Keyboards):
    try:
        db.session.delete(keyboard)
        db.session.commit()
        return keyboard_schema.dump(keyboard)
    except Exception as e:
        db.session.rollback
        raise e


def update(keyboard: Keyboards):
    try:
        db.session.commit()
        return keyboard_schema.dump(keyboard)
    except Exception as e:
        db.session.rollback()
        raise e
