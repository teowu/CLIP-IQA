# Copyright (c) OpenMMLab. All rights reserved.
from .generation_inference import generation_inference
from .inpainting_inference import inpainting_inference
from .matting_inference import init_model, matting_inference, init_coop_model
from .restoration_face_inference import restoration_face_inference
from .restoration_inference import restoration_inference, restoration_demo_inference, restoration_noisy_inference
from .restoration_video_inference import restoration_video_inference
from .test import multi_gpu_test, single_gpu_test
from .train import set_random_seed, train_model

__all__ = [
    'train_model', 'set_random_seed', 'init_model', 'matting_inference',
    'inpainting_inference', 'restoration_inference', 'generation_inference',
    'multi_gpu_test', 'single_gpu_test', 'restoration_video_inference',
    'restoration_face_inference', 'init_coop_model', 'restoration_demo_inference', 'restoration_noisy_inference'
]
