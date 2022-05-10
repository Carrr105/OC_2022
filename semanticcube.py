#left op que contiene right op que contiene operador con su resultado
semantic = {
  'int': {
    'int': {
      '+': 'int',
      '-': 'int',
      '*': 'int',
      '/': 'float',
      '&&': 'int',
      '||': 'int',
      '>': 'int',
      '<': 'int',
      '<=': 'int',
      '>=': 'int',
      '!=': 'int',
      '==': 'int',
      '=': 'int'
    },
    'float': {
      '+': 'float',
      '-': 'float',
      '*': 'float',
      '/': 'float',
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
    }
  },
  'float': {
    'float': {
      '+': 'float',
      '-': 'float',
      '*': 'float',
      '/': 'float',
      '&&': 'int',
      '||': 'int',
      '>': 'int',
      '<': 'int',
      '<=': 'int',
      '>=': 'int',
      '!=': 'int',
      '==': 'int',
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
          '&&': 'int',
          '||': 'int',
          '>': 'int',
          '<': 'int',
          '<=': 'int',
          '>=': 'int',
          '!=': 'int',
          '==': 'int',
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
      }
  }
}
    
def get_type(self, leftop, rightop, op):
    return semantic[leftop][rightop][op]