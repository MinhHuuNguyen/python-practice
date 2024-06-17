# 1. Download carvana_image_masking_dataset
bash data/download_data.sh

# 2. Download checkpoint
bash download_ckpt.sh

# 3. Create environment for Pytorch-UNet
python3 -m venv Pytorch-UNet_env
. ./Pytorch-UNet_env/bin/activate
pip3 install -r additional_requirements.txt
cd Pytorch-UNet
pip3 install -r requirements.txt

# 4. Run carvana_image_masking_dataset visualization

# 5. Infer Pytorch-UNet pretrained model with ./data/carvana_image_masking_dataset/test
python predict.py --model ../carvana_image_masking_ckpt/carvana_image_masking_scale1.0_epoch2.pth \
    --input ../data/carvana_image_masking_dataset/test/0a84dac5df69_03.jpg \
    --output ./0a84dac5df69_03_OUT.jpg \
    --viz

# 6. Train Pytorch-UNet model with carvana_image_masking_dataset
python train.py --epochs 5 --batch-size 1
