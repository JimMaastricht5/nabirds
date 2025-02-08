# MIT License
#
# 2024 Jim Maastricht
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# reads the NABirds text files and filters the contents based on the file filter.txt
# jimmaastricht5@gmail.com
import csv

def filter_images():
    """
    function loads a file from the current directory call filter.txt
    Processes through rows and uses the class keys in this file to limit the
    images, image_class_labels, and train_test_split files to only the desired classes in filter.txt
    :return:
    """
    species_class_set = set()
    image_class_set = set()
    with open('filter.txt', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # read in named cols
        for row in reader:
            class_num = int(row['class'])
            species_class_set.add(class_num)

    with open('image_class_labels.txt', 'r', encoding='utf-8') as infile, open('image_class_labels_filtered.txt', 'w',
                                                                               encoding='utf-8') as outfile:
        for line in infile:
            image_key, class_num = line.strip().split() # Split each line on whitespace
            class_num = int(class_num)
            if class_num in species_class_set:  # Check if class is in the set
                outfile.write(line)
                image_class_set.add(image_key)

    with open('images.txt', 'r', encoding='utf-8') as infile, open('images_filtered.txt', 'w',
                                                                   encoding='utf-8') as outfile:
        for line in infile:
            image_key, image_name = line.strip().split()
            if image_key in image_class_set:
                outfile.write(line)

    with open('train_test_split.txt', 'r', encoding='utf-8') as infile, open('train_test_split_filtered.txt', 'w',
                                                                             encoding='utf-8') as outfile:
        for line in infile:
            image_key, test_train_boolean = line.strip().split()
            if image_key in image_class_set:
                outfile.write(line)


if __name__ == "__main__":
    filter_images()
    print('Done')