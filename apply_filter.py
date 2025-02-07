import csv

def filter_images():
    species_class_set = set()
    image_class_set = set()
    with open('filter.txt', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # read in named cols
        for row in reader:
            class_num = int(row['class'])
            species_class_set.add(class_num)

    with open('image_class_labels.txt', 'r', encoding='utf-8') as infile, open('image_class_labels_filtered.txt', 'w', encoding='utf-8') as outfile:
        for line in infile:
            image_key, class_num = line.strip().split()
            class_num = int(class_num)
            if class_num in species_class_set:  # Check if class is in the set
                outfile.write(line)
                image_class_set.add(image_key)

    with open('images.txt', 'r', encoding='utf-8') as infile, open('images_filtered.txt', 'w', encoding='utf-8') as outfile:
        for line in infile:
            image_key, image_name = line.strip().split()  # Split each line on whitespace
            if image_key in image_class_set:
                outfile.write(line)

    with open('train_test_split.txt', 'r', encoding='utf-8') as infile, open('train_test_split_filtered.txt', 'w', encoding='utf-8') as outfile:
        for line in infile:
            image_key, test_train_boolean = line.strip().split()  # Split each line on whitespace
            if image_key in image_class_set:
                outfile.write(line)

filter_images()
print('Done')