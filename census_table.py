from copy import copy
import sqlalchemy as sa
from sqlalchemy.sql import and_, or_, not_, func, true
from anytree import Node, RenderTree
from anytree.iterators import PreOrderIter
from schema import hh_persons
from predicate import Predicate


class CensusTable():
    '''
    This is a class for representing an SF1 "table" of queries
    '''

    def __init__(self, table_no):

        self.table_no = table_no        # identifier of table, e.g. "P1."
        self.root_select = None         # SQLAlchemy select object consistent with universe
        self.root = Predicate(name='Total', pred=true(), parent=None) # root entry applies 'True' predicate
        self.meta_data = {}             # dictionary holding metadata e.g. {'PL-94':True} (maybe used later?)


    def add_ortho_level(self, pred_list):
        '''
        Add orthogonal level
        add each predicate in pred_list to every leaf
        '''
        leaves = [n for n in PreOrderIter(self.root, filter_=lambda n: n.is_leaf is True)]
        for l in leaves:
            for p in pred_list:
                copy(p).parent = l


    def entries(self):
        '''
        Returns an iterator over each of the table entries in order.  E.g. usually a Total first,
        '''
        return PreOrderIter(self.root)


    def set_root_select(self, choice_string):
        if choice_string == 'population':
            # for population queries
            self.root_select = sa.select([func.count().label('cnt')]).select_from(hh_persons)
        else:
            raise Exception('invalid root select choice')


    def render(self, sql=False):
        print(self.root_select)
        for pre, fill, node in RenderTree(self.root):
            print("%s%s:\t%s" % (pre,
                                 node.name,
                                 node.pred.compile(compile_kwargs={"literal_binds": True})))
            if sql:
                stmt = str(node.sql(self.root_select)).split('\n')
                for line in stmt:
                    print("%s.  %s" % (fill, line))
