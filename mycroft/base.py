import copy

class BaseWorker(object):
    """
    Base class for Mycroft Workers. Workers accept an arbitrary set of keyword arguments.
    Use these to configure worker instances.

    Attributes:
        name (str): The name of your worker
    """

    def __init__(self, name = None,**kwargs ):

        if name is None:
            name = self.__class__.__name__

        self.name = name
        self.set_params(**kwargs)

    def execute(self, x = None):
        """
         Workers are expected to supply an execute method. This method will be called when the worker is run.
         Each execution operates on an mutates on a single input variable x.
        """

        raise NotImplementedError('You must implement an execute method')

        return x

    def get_param(self, param):
        return getattr(self, param)

    def preview(self, x=None):
        """
         Workers are may supply a preview method. This method delivers representative outputs without
         mutating the input variable.

        """
        raise NotImplementedError('Implement a preview method to provide a preview of the workers outputs')

        y = copy.deepcopy(x)

        return y

    def set_params(self, **params):
        for key,value in list(params.items()):

            setattr(self, key, value)

        return self

class BaseDataObject (object):
    """

    Base class for describing data objects
    """

    def __init__ (self, name, *children, **kwargs):

        if name is None:
            name = self.__class__.__name__

        self.name = name
        self.parent = None
        self.set_params(**kwargs)
        self.children = {}
        for i in children:
            self[i.name] = i

    def get_param(self, param):
        return getattr(self, param)


    def __getitem__(self,item):

        return self.children[item]

    def __setitem__(self, key, value):

        self.children[key] = value
        self.children[key].set_parent(self)
        # override default name with key
        if value.name == value.__class__.__name__:
            value.name = key

    def set_params(self, **params):
        for key,value in list(params.items()):

            setattr(self, key, value)

        return self

    def set_parent(self,parent):

        self.parent = parent


class Pipeline(object):
    """
    Pipelines are one of the ways of composing multistage tasks. A pipeline is initialized
    using a sequence of workers.

    The sequence of workers are described using positional arguments.

    """

    def __init__(self, *args,**kwargs ):

        self.workers = list(args)
        self.set_params(**kwargs)

    def execute(self, x = None):
        """
         Chain the workers by calling the execute method of each worker and passing the output
         of the stage as the input to the next.
        """

        for w in self.workers:
            x = w.execute(x)

        return x

    def get_param(self, param):
        return getattr(self, param)

    def set_params(self, **params):
        for key,value in list(params.items()):

            setattr(self, key, value)

        return self

