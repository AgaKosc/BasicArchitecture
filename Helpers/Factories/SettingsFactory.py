from Settings.ProductionSettings import ProductionSettings


class SettingsFactory:

    @staticmethod
    def getSettings(env):
        if env == 'prod':
            return ProductionSettings()
        raise Exception("No such '{0}' env exists".format(env))
