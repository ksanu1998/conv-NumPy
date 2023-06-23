#!/usr/bin/env python
# coding: utf-8

import numpy as np

class KLDivLoss:
    ''' Computes Kullback-Leibler (KL) Divergence Loss given the input and target '''
    
    ''' * The class implementation will be along the lines of torch.nn.MSELoss in order to 
          enable comparison of this NumPy only implementation and seamless testing
        * Can expect extensive refactoring of the existing code in the days to come
        * As part of refactoring, some code will be de-modularized
        * Old code will be retained at the end of the notebook for reference
    '''
    '''
        TODO:
        * Replace `torch.round()` with `np.allclose()` for tests
        * Optimizing code
    '''
    
    def __init__(
        self,
        size_average = None,
        reduce = None,
        reduction = 'mean',
        log_target = False,
        verbose = False
        ):
        super(KLDivLoss, self).__init__()
        
        ''' mandatory parameters '''
        # None
        
        ''' optional parameters '''
        self.reduction = reduction
        self.log_target = log_target
        
        ''' optional parameters (dummy, yet to be implemented)'''
        self.size_average = size_average
        self.reduce = reduce
        
        ''' additional parameters (different from torch.nn.Conv2D)'''
        self.verbose = verbose
        self.verboseprint = print if self.verbose else lambda *a, **k: None
        self.verboseprint('*** parameters ***')
        self.verboseprint('size_average: {}, reduce: {}, reduction: {}, log_target: {}'.format(self.size_average, self.reduce, self.reduction, self.log_target))
        self.verboseprint('\n')
    
    def forward(self, _input, _target):
        ''' forward pass to compute KL Divergence Loss'''
        
        ''' error checking '''
        if not (isinstance(_input, int) or isinstance(_input, float) or isinstance(_input, np.ndarray)):
            raise Exception('invalid input: `input` should either be an int, a float, or a NumPy ndarray')
        
        if not (isinstance(_target, int) or isinstance(_target, float) or isinstance(_target, np.ndarray)):
            raise Exception('invalid input: `target` should either be an int, a float, or a NumPy ndarray')
            
        if (isinstance(_input, np.ndarray) and not isinstance(_target, np.ndarray))  or (not isinstance(_input, np.ndarray) and isinstance(_target, np.ndarray)):
            raise Exception('invalid input: `input` and `target` should both be a NumPy ndarray, or can be a mix of `int` and `float`')
            
        ''' compute KL Divergence Loss '''
        if not self.log_target:
            output = _target * (np.log(_target) - _input)
        else:
            output = np.exp(_target) * (_target - _input)
        if self.reduction == 'mean':
            output = np.mean(output)
        # elif self.reduction == 'batchmean':
            # if isinstance(_input, np.ndarray):
                # print(_input.size())
        elif self.reduction == 'sum':
            output = np.sum(output)
        elif self.reduction == 'none':
            pass
        else:
            raise Exception("invalid input: `reduction` flag should be one of `'mean'`, `'sum'`, `'batchmean'` or `'none'`")
        self.verboseprint("*** KLDivLoss output ***")
        self.verboseprint(output)
        self.verboseprint('\n')
        return output