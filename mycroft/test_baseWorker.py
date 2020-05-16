import pytest
import mycroft.base as mc

#setup objects for tests
worker = mc.BaseWorker() # default
worker2 = mc.BaseWorker('Fred',alpha=62, beta='b') #with name and custom params

class Incrementor(mc.BaseWorker):

    """
    Simple worker. Increments a number by a value. Value is passed as a parameter called increment)
    """

    def __init__(self, name = None, increment = 1, **kwargs):

        kwargs['increment'] = increment
        super().__init__(name, **kwargs)

    def execute(self, x):
        """
        Execute the worker. The execute method always takes a single argument representing the
        input to the worker.
        """

        return (x + self.increment)

worker3 = Incrementor('add_two',2)   # custom worker object

# create a text pipeline that uses a sequence of two incrementors. The first adds 2. The next adds 3.
pipeline = mc.Pipeline(worker3,Incrementor('add_three',3))


def test_init():
    assert(worker.__class__.__name__ == 'BaseWorker')

def test_set_params():
    worker.set_params(alpha = 5, beta = 'a')
    assert(worker.alpha == 5)
    assert(worker.beta == 'a')

def test_set_params_on_init():
    assert(worker2.alpha == 62)
    assert(worker2.beta == 'b')

def test_get_param():
    assert(worker.get_param('alpha') == 5)
    assert(worker.get_param('beta') == 'a')

def test_execute():
    with pytest.raises(Exception):
        worker.execute()

def test_Incrementor():
    assert (worker3.execute(1) == 3)

def test_pipeline():
    assert (pipeline.execute(5) == 10)