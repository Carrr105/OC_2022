# falta implementar con bool
class SemanticCube :

  def __init__(self):
    #left op que contiene right op que contiene operador con su resultado
    semantic = {
      'int': {
        'int': {
          '+': 'int',
          '-': 'int',
          '*': 'int',
          '/': 'float',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'bool',
          '<': 'bool',
          '<=': 'bool',
          '>=': 'bool',
          '!=': 'bool',
          '==': 'bool',
          '=': 'int'
        },
        'float': {
          '+': 'float',
          '-': 'float',
          '*': 'float',
          '/': 'float',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'bool',
          '<': 'bool',
          '<=': 'bool',
          '>=': 'bool',
          '!=': 'bool',
          '==': 'bool',
          '=': 'int'
        },
        'char': {
          '+': 'ERROR',
          '-': 'ERROR',
          '*': 'ERROR',
          '/': 'ERROR',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'ERROR',
          '<': 'ERROR',
          '<=': 'ERROR',
          '>=': 'ERROR',
          '!=': 'ERROR',
          '==': 'ERROR',
          '=': 'ERROR'
        },
        'bool': {
          '+': 'ERROR',
          '-': 'ERROR',
          '*': 'ERROR',
          '/': 'ERROR',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'ERROR',
          '<': 'ERROR',
          '<=': 'ERROR',
          '>=': 'ERROR',
          '!=': 'ERROR',
          '==': 'ERROR',
          '=': 'ERROR'
        }
      },
      'float': {
        'float': {
          '+': 'float',
          '-': 'float',
          '*': 'float',
          '/': 'float',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'bool',
          '<': 'bool',
          '<=': 'bool',
          '>=': 'bool',
          '!=': 'bool',
          '==': 'bool',
          '=': 'float'
        },
        'char': {
          '+': 'ERROR',
          '-': 'ERROR',
          '*': 'ERROR',
          '/': 'ERROR',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'ERROR',
          '<': 'ERROR',
          '<=': 'ERROR',
          '>=': 'ERROR',
          '!=': 'ERROR',
          '==': 'ERROR',
          '=': 'ERROR'
        },
        'int': {
          '+': 'float',
          '-': 'float',
          '*': 'float',
          '/': 'float',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'bool',
          '<': 'bool',
          '<=': 'bool',
          '>=': 'bool',
          '!=': 'bool',
          '==': 'bool',
          '=': 'float'
        },
        'bool': {
          '+': 'ERROR',
          '-': 'ERROR',
          '*': 'ERROR',
          '/': 'ERROR',
          '&&': 'ERROR',
          '||': 'ERROR',
          '>': 'ERROR',
          '<': 'ERROR',
          '<=': 'ERROR',
          '>=': 'ERROR',
          '!=': 'ERROR',
          '==': 'ERROR',
          '=': 'ERROR'
        }
      },
      'char': {
          'char': {
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'char'
          },
          'int':{
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'ERROR'  
          },
          'float': {
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'ERROR'  
          },
          'bool': {
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'ERROR'  
          }
      },'bool': {
          'char': {
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'ERROR'
          },
          'int':{
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'ERROR'  
          },
          'float': {
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'ERROR',
              '||': 'ERROR',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'ERROR',
              '==': 'ERROR',
              '=': 'ERROR'  
          },
          'bool': {
              '+': 'ERROR',
              '-': 'ERROR',
              '*': 'ERROR',
              '/': 'ERROR',
              '&&': 'bool',
              '||': 'bool',
              '>': 'ERROR',
              '<': 'ERROR',
              '<=': 'ERROR',
              '>=': 'ERROR',
              '!=': 'bool',
              '==': 'bool',
              '=': 'bool'  
          }
      }
    }

    def get_type(self, leftop, rightop, op):
      return semantic[leftop][rightop][op]