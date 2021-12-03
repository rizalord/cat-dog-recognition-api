from dependency_injector import containers, providers
from app.services.predict_service import PredictService

class Container (containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "app.controllers.predict_controller",
    ])
    config = providers.Configuration()

    predict_service = providers.Singleton(PredictService)
