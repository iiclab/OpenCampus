# OpenCampus

this is programs for OpenCampus

## fast-style-transfer

style transfer demo.

This is based on https://github.com/lengstrom/fast-style-transfer

Firstly, you need to clone from above repository.
Then, files in "fast-style-transfer" of this repository are moved to above original repository.

* evaluate_webcam.py ... This is realtime demo using webcamera.
* demo_webcam.sh ... *The usage of evaluate_webcam.py*
* make_outputImage.py ... This makes image containing content.jpg, style.jpg, generated-image.py .
                          Each images resized to fixed size.
  `
    python make_outputImage.py --content $content_image_file_name \
                               --create $created_image_file_name_by_evaluate.jpg \
			       --style $style_image_file_name \
			       --out $output_file_name
`

* make_outputImage2.py ... same as make_outputImage.py
                           The difference is that this keeps original image's scale ratio.

* run_all.sh ... Usages of evaluate.py & make_output_image.py
  
 Usage
  `sh run_all.sh`
* run_train.sh ... Usage for training model
  `sh run_train.sh`

## keras-yolo3

YOLO-v3 implemented with Keras.

This is based on https://github.com/qqwweee/keras-yolo3

Firstly, you need to clone from above repository.
Then, files in "keras-yolo3" of this repository are moved to above original repository.

* yolo_webcam.py ... Realtime object detection with **YOLO-v3** implemented with Keras.
`python yolo_webcam.py`

* yolo_tiny_webcam.py ... Realtime objected detection with **Tiny-YOLO-v3**.
`python yolo_tiny_webcam.py`
