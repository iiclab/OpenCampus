# This is for consistent processing
#  containing training, evaluate and output


Style_image=examples/style/wave.jpg
#Content_image=examples/content/stata.jpg
Content_image=kiminonaha.jpg
Create_image=out3.jpg
Out_image=my_create.png

# For Training

#python style.py \
#    --style ${Style_image} \
#    --checkpoint-dir checkpoint_dir \
#    --test ${In_image} \
#    --test-dir output \
#    --content-weight 1.5e1 \
#    --checkpoint-iterations 1000 \
#    --batch-size 20

# For Evaluate
python evaluate.py \
    --checkpoint checkpoint_dir/fns.ckpt \
    --in-path ${Content_image} \
    --out-path ${Create_image}

python make_outputImage2.py \
       --content ${Content_image} \
       --create ${Create_image} \
       --style ${Style_image} \
       --out ${Out_image}
