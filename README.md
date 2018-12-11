ICNS-Self-Driving
=================

### Generate CSV file :
 ```python xml_to_csv.py --xml_path=xml --test_size=0.5```

### Generate TF Record file :
  ```python generate_tfrecord.py --csv_input=data/train.csv  --output_path=data/train.record --image_dir=images```

  ```python generate_tfrecord.py --csv_input=data/test.csv  --output_path=data/test.record --image_dir=images```
