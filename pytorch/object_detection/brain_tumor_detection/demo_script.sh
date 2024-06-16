# 1. Download COCO dataset
bash yolov5/data/scripts/get_coco.sh

# 2. Download brain_tumor_dataset
bash data/download_data.sh

# 3. Run brain_tumor_detection_visualization.ipynb

# 4. Create environment for yolov5
python3 -m venv yolov5_env
. ./yolov5_env/bin/activate
pip3 install -r additional_requirements.txt
cd yolov5
pip3 install -r requirements.txt

# 5. Infer yolov5 pretrained model with yolov5/data/images
python3 detect.py --weights yolov5s.pt --source data/images/bus.jpg
python3 detect.py --weights yolov5s.pt --source data/images/zidane.jpg --save-txt --save-conf --save-crop

# 6. Infer yolov5 pretrained model with data/test_image_1.jpg
python3 detect.py --weights yolov5s.pt --source ../data/test_images/ --save-txt --save-conf --save-crop

# 6. Run brain_tumor_detection_create_coco_dataset.ipynb

# 7. Train yolov5 model with brain_tumor_dataset
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5n.yaml  --batch-size 4
python train.py --data ../brain_tumor_coco.yaml --epochs 300 --weights '' --cfg yolov5n.yaml  --batch-size 4

# 8. Infer yolov5 trained model
