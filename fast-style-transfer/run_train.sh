python style.py \
    --style examples/style/wave.jpg \
    --checkpoint-dir checkpoint_dir \
    --test examples/content/chicago.jpg \
    --test-dir output \
    --content-weight 1.5e1 \
    --checkpoint-iterations 1000 \
    --batch-size 20 \
    --epochs 1

