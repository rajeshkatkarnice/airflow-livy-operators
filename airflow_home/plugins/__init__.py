from airflow.plugins_manager import AirflowPlugin

from .livy_batch_plugin import LivyBatchOperator, LivyBatchSensor
from .livy_session_plugin import (
    LivySessionCreationSensor,
    LivySessionOperator,
    LivyStatementSensor,
)


class LivyBatchPlugin(AirflowPlugin):
    name = "Livy batch plugin"
    sensors = [LivyBatchSensor]
    operators = [LivyBatchOperator]


class LivySessionPlugin(AirflowPlugin):
    name = "Livy session plugin"
    sensors = [LivySessionCreationSensor, LivyStatementSensor]
    operators = [LivySessionOperator]
