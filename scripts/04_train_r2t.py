#!/usr/bin/env python
# Phase 3: Main experiment. Loads D_0_clean_10k.jsonl.
# Uses the custom dataset from src.r2t.dataset.
# Trains the model defined in src.r2t.model with the dual (text+graph) loss.
# Remembers to use torch.device('mps') on your Mac!
# Saves the final model to models/r2t_model.pt
