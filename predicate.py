from anytree import Node
from sqlalchemy.sql import and_, or_, not_, func, true


class Predicate(Node):
    '''
    A Predicate object represents a node in the hierarchy defined by a census table.
    It holds a boolean condition on one or more attributes

    This class inherits from anytree.Node to provide some tree methods.
    '''

    def __init__(self, name, pred=None, parent=None):
        self.name = name    # readable name, only for display purposes
        self.pred = pred    # an sqlalchemy predicate, usually instance of sqlalchemy.sql.expression.BinaryExpression
        self.parent = parent    # reference to parent node


    def condition(self):
        '''
        This constructs an sqlalchemy conjunction of this predicate with all its ancestors.
        '''
        return and_(*[p.pred for p in self.ancestors], self.pred)


    def sql(self, select):
        '''
        input: an sqlalchemy select representing the base table conjunctions will be added to.
        output: sql expression which will compute the count corresponding to the entry represented by this predicate
        (This can't be a method of Predicate because it needs to
        '''
        return select.where(self.condition()).compile(compile_kwargs={"literal_binds": True})
