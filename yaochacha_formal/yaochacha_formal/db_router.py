# coding-utf-8


class app01Router(object):
    """
    A router to control all database operations on models in the app01 application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read app02 models go to 39net DB.
        """
        if model._meta.app_label == 'app01':
            return '39net'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write app02 models go to 39net DB.
        """
        if model._meta.app_label == 'app01':
            return '39net'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the app01 app is involved.
    #     """
    #     if obj1._meta.app_label == 'app01' or \
    #        obj2._meta.app_label == 'app01':
    #         return True
    #     return None
    #
    # def allow_migrate(self, db, model):
    #     """
    #     Make sure the app01 app only appears in the 39net database.
    #     """
    #     if db == '39net':
    #         return model._meta.app_label == 'app01'
    #     elif model._meta.app_label == 'app01':
    #         return False
    #
    # def allow_syncdb(self, db, model):
    #     if db == '39net' or model._meta.app_label == "app01":
    #         return False  # we're not using syncdb on our 39net database
    #     else:  # but all other models/databases are fine
    #         return True


class app02Router(object):
    """
    A router to control all database operations on models in the app02 application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read app02 models go to apps DB.
        """
        if model._meta.app_label == 'app02':
            return 'apps'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write app02 models go to apps DB.
        """
        if model._meta.app_label == 'app02':
            return 'apps'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the app02 app is involved.
    #     """
    #     if obj1._meta.app_label == 'app02' or \
    #        obj2._meta.app_label == 'app02':
    #         return True
    #     return None
    #
    # def allow_migrate(self, db, model):
    #     """
    #     Make sure the app02 app only appears in the apps database.
    #     """
    #     if db == 'apps':
    #         return model._meta.app_label == 'app02'
    #     elif model._meta.app_label == 'app02':
    #         return False
    #
    # def allow_syncdb(self, db, model):
    #     if db == 'apps' or model._meta.app_label == "app02":
    #         return False  # we're not using syncdb on our apps database
    #     else:  # but all other models/databases are fine
    #         return True
