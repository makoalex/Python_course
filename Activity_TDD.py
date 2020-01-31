# making functions to test TDD with Unittest
def healthy(food, is_healthy):
    """eating nutritious is the first step toa """
    if not  isinstance(is_healthy, bool):
        raise ValueError('is_healthy must be a bool')
    ending = 'because my body is a temple'

    if not is_healthy:
        return "I'm eating {} because YOLO".format(food)
    return "I'm eating {} {} ".format(food, ending)


def train(num_days):
    """ training hard os good for the body and mind"""
    if num_days >= 3:
        return "i feel  good after {} days of training".format(num_days)

    return '{} time a week  is not enough training for a healthy body'.format(num_days)


