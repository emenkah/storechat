from celery.decorators import task
from celery.utils.log import get_task_logger
from .notifications import notification
import datetime


logger = get_task_logger(__name__)


@task(name="send_notification_email_task")
def send_notification_email_task(subject, body, discount_code, client_name,  operator_first_name, dest_email):
    execution_time = datetime.datetime(2021,10,25,10, 56)
    logger.info("Sent chat to client")
    return notification(subject, body, discount_code, client_name,  operator_first_name, dest_email).apply_async(eta=execution_time)

