# 1. Create environment for SegmentAnything
python3 -m venv segment_anything_env
. ./segment_anything_env/bin/activate
pip3 install git+https://github.com/facebookresearch/segment-anything.git
pip3 install opencv-python==4.9.0.80 pycocotools==2.0.7 matplotlib==3.9.0 onnxruntime==1.18.0 onnx==1.16.1
pip3 install jupyter==1.0.0 torch==1.9.0 torchvision==0.10.0 numpy==1.23
