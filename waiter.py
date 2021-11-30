import logging
import time

logging.basicConfig(level="INFO")
logger = logging.getLogger("script")


def wait(predicate, timeout=10, poll_interval=1, condition_msg="true"):
    """
    A waiting method that runs a loop
    :param predicate:
    :param timeout:
    :param poll_interval:
    :param condition_msg:
    :return:
    """
    start_time = time.monotonic()

    while time.monotonic() - start_time <= timeout:
        try:
            if predicate():
                return
        except Exception:
            logger.exception("Cannot execute the predicate")
        logger.warning(f"Waiting for %s", condition_msg)
        time.sleep(poll_interval)
    raise RuntimeError(f"Too long wait for {condition_msg}")
