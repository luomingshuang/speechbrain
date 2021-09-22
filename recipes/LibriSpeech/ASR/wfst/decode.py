#!/usr/bin/env/python3
"""
Recipe for using the k2 for WFST decoding on LibriSpeech 
based on the AM trained by speechbrain.
In this recipe, the AM is from other ASR recipes 
(ctc, seq2seq, transducer and transformer) 
or the pretrained AM models which can be downloaded on LibriSpeech.

To run this recipe, do the following:
> CUDA_VISIBLE_DEVICES='0' python decode.py hparams/config.yaml

In this recipe, we won't display how to use k2 to train a 
ASR system with librispeech. If you want to know it, you can konw 
many details about k2 and its recipes from the following urls:
https://github.com/k2-fsa/k2
https://github.com/k2-fsa/icefall

"""
